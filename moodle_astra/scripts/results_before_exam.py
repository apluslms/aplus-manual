import argparse
import sys
import json
import csv
import datetime
import yaml # requires pip package PyYAML (used by the MOOC grader as well)

# This script writes a CSV file based on the result JSON file exported from the
# Moodle Astra plugin. The CSV file may be imported to spreadsheet software
# such as Excel. The CSV file may include all students with their exercise
# points, or it may be filtered to only include students who passed the mandatory
# exercises. You may also set a date so that only submissions submitted before
# that date are included in the results. The output may be filtered to only
# list the student identifiers without any points.
#
# If you want to take only submissions submitted before a certain date into
# account, you must include all submissions when exporting the results from
# Astra. This script can only work with the data available in the supplied
# JSON file.
#
# The default output CSV format: student id, passed (0 or 1), course total points,
# round1 total, exercise points in round1 for each exercise,
# round2 total, exercises of round2,...
#
#
# invocation: python3 results_before_exam.py JSON_FILE INDEX_YAML_FILE OUTPUT_CSV
# where JSON_FILE is the path to the results JSON file exported from Astra,
# INDEX_YAML_FILE is the path to the MOOC grader course configuration file (index.yaml)
# (in RST courses, it is located in _build/yaml/index.yaml),
# and OUTPUT_CSV is the path to the output file that will be written here
# (for example, results.csv).
# Additional options are listed when you invoke with --help argument.


def write_csv(csv_filename, fieldnames, data, include_header=True):
    # fieldnames parameter is a sequence of keys that identify the order
    # in which values are written to the CSV file.
    # data is a list of dicts.
    # Each dict corresponds to one record and maps fieldnames to values.
    # The keys in the dict must match the fieldnames strings
    # (if a key is missing, the CSV uses an empty string for the value).
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='', extrasaction='ignore')
        if include_header:
            writer.writeheader()
        writer.writerows(data)


def parse_results(results_json, indexyaml_path, submitted_before=None, include_only_passed_students=True):
    # submitted_before: only include submissions that were submitted before this time.
    # Type: Unix timestamp (integer). If None, all submissions are included.
    # include_only_passed_students: if True, only include students that passed mandatory exercises.
    # (index.yaml is used to define which exercises are mandatory. Basically,
    # it checks the module points to pass limit.)
    data = []
    with open(indexyaml_path) as f:
        index = yaml.safe_load(f)

    '''
    JSON structure in the top level:
    {
        "students" : {
            "<student_id>" (idnumber or username): {
                "exercises": {}, # see below for details
                "rounds": {},
                "categories": {}
            }
        },
        "numberofstudents": 5
    }
    '''
    for student, sres in results_json['students'].items():
        record = {} # one line in a CSV file
        record['student'] = student
        record['coursetotal'] = 0
        for key, exresults in sres['exercises'].items():
            '''
            key has the format "roundkey/exercisekey"
            exresults dictionary has the structure:
            {
                "points": 10, (points of the best submission)
                "submissiontime": Unix timestamp,
                "numberofsubmissions": 5,
                "id": 1, (database ID of the submission)
                "roundkey": "someround",
                "submissions": [ (each submission listed if all submissions are included in the JSON)
                    {
                    "points": 5,
                    "submissiontime": timestamp,
                    "status": "ready",
                    "id": 1 (database ID of the submission)
                    }
                ]
            }
            '''
            round_key = exresults['roundkey']
            exercise_key = key[len(round_key) + 1:] # key has the format "roundkey/exercisekey"

            if submitted_before is None:
                exercise_points = exresults['points'] # best points from all submissions
            else:
                best_sbms = get_best_submission_submitted_before(exresults['submissions'], submitted_before)
                exercise_points = best_sbms['points'] if best_sbms else 0
            record['_ex_' + exercise_key] = exercise_points

            if ('_r_' + round_key) in record:
                record['_r_' + round_key] += exercise_points # total points of the round
            else:
                record['_r_' + round_key] = exercise_points
            record['coursetotal'] += exercise_points

        passed_rounds = {}
        for module in index['modules']:
            round_key = module['key']
            round_points_to_pass = module.get('points_to_pass', 0)
            passed_rounds[round_key] = record.get('_r_' + round_key, 0) >= round_points_to_pass
        passed_all = all(iter(passed_rounds.values()))
        record['passed'] = int(passed_all)
        if passed_all or not include_only_passed_students:
            data.append(record)

    # Sort the list by student ids.
    data.sort(key=lambda rec: rec['student'])
    return data


def get_best_submission_submitted_before(submissions, submitted_before):
    # submitted_before is a Unix timestamp (integer)
    best = None
    for sbms in submissions:
        if sbms['submissiontime'] < submitted_before and \
                (best is None or sbms['points'] > best['points']):
            best = sbms
    return best


def read_csv_fieldnames_from_index_yaml(indexyaml_path):
    fieldnames = ['student', 'passed', 'coursetotal']
    with open(indexyaml_path) as f:
        index = yaml.safe_load(f)
    # rounds and their exercises
    for module in index['modules']:
        round_key = module['key']
        fieldnames.append('_r_' + round_key)
        for exercise in module.get('children', []):
            exercise_key = exercise['key']
            if not exercise.get('static_content', False):
                # it is an exercise, not a content chapter
                fieldnames.append('_ex_' + exercise_key)
            else:
                # Check if the chapter has child exercises.
                # Actually, exercises could be nested in arbitrarily deep levels, but usually
                # there are only two levels and that is assumed here.
                for childex in exercise.get('children', []):
                    fieldnames.append('_ex_' + childex['key'])

    return fieldnames


def parse_json(filepath):
    with open(filepath) as f:
        return json.load(f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Write a CSV file containing the results of the course.")
    parser.add_argument("results_json_file", help="Path to the JSON file that contains the exercise submission data " \
        "(the JSON file should be exported from Astra with all submissions included).")
    parser.add_argument("index_yaml", help="Path to the MOOC grader course configuration file (index.yaml).")
    parser.add_argument("output_csv", help="Path to the output CSV file that will be written by this script.")
    parser.add_argument("-t", "--submitted-before",
        help="If given, only submissions submitted before this time are included. "
             "Time format example: '2019-01-24 23:59 +0200'")
    parser.add_argument("-p", "--only-passed-students", action="store_true",
        help="If this flag is given, the output file includes only students who "
             "passed mandatory exercises (based on the module points to pass limits).")
    parser.add_argument("-n", "--no-points-output", action="store_true",
        help="If this flag is given, the output file contains only a list of students without their exercise points.")
    args = parser.parse_args()
    try:
        submitted_before = None
        if args.submitted_before:
            # Convert the date to a Unix timestamp (integer).
            submitted_before = datetime.datetime.strptime(args.submitted_before, "%Y-%m-%d %H:%M %z").timestamp()

        json = parse_json(args.results_json_file)
        data = parse_results(json, args.index_yaml, submitted_before=submitted_before,
            include_only_passed_students=args.only_passed_students)
        if args.no_points_output:
            fieldnames = ['student']
        else:
            fieldnames = read_csv_fieldnames_from_index_yaml(args.index_yaml)
        write_csv(args.output_csv, fieldnames, data, include_header=not args.no_points_output)
    except json.JSONDecodeError as e: # the exception was added in Python 3.5
        print("Error: the argument {0} is not a valid JSON document".format(sys.argv[1]))
        print(e)
        sys.exit(2)
    except Exception as e:
        print(e)
        sys.exit(2)

