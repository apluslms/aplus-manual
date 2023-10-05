import argparse
import json
import os
import re
import shutil
import subprocess
import yaml


PERSONALIZED_CONTENT_DIR = 'personalized_exercises' # Same as MOOC-Grader settings.py 'PERSONALIZED_CONTENT_DIR'


class ExerciseGenerationError(Exception):
    pass


def pregenerated_exercises_directory_path(exercise):
    '''
    Return path to the directory of pregenerated exercise instances
    (instances are directories under this directory).
    '''
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), PERSONALIZED_CONTENT_DIR, exercise["key"])


def prepare_pregenerated_exercises_directory(exercise):
    '''
    Create the base directory for pregenerated exercise instances.
    '''
    pregen_dir = pregenerated_exercises_directory_path(exercise)
    # Create an empty directory unless it exists already
    try:
        os.makedirs(pregen_dir)
    except OSError:
        return # It exists


def pregenerated_exercise_instances(exercise):
    '''
    Return a list of the existing pregenerated exercises instances (directory names).
    '''
    pregenerated_dir = pregenerated_exercises_directory_path(exercise)
    try:
        # Return a list of directory names (not full paths)
        return [instance_dir for instance_dir in os.listdir(pregenerated_dir)
                if os.path.isdir(os.path.join(pregenerated_dir, instance_dir))]
    except OSError:
        return [] # pregenerated_dir does not exist


def delete_pregenerated_exercise_instances(exercise):
    '''
    Delete pregenerated exercise instances (directories).
    '''
    pregen_dir = pregenerated_exercises_directory_path(exercise)
    try:
        for entry in os.listdir(pregen_dir):
            # Only delete directories under the parent directory
            file_path = os.path.join(pregen_dir, entry)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
    except OSError:
        pass # The directory may not exist yet


def generate_exercise_instances(exercise, number_of_instances):
    '''
    Generate the given number of new exercise instances.
    '''
    existing_instances = pregenerated_exercise_instances(exercise)
    # Instance directories are named with integers, find the next unused integer
    index = -1
    for inst in existing_instances:
        try:
            inst = int(inst)
            if inst > index:
                index = inst
        except ValueError:
            pass
    index += 1

    pregen_dir = pregenerated_exercises_directory_path(exercise)
    # This base directory should already exist
    for _ in range(number_of_instances):
        instance_path = os.path.join(pregen_dir, str(index))
        os.mkdir(instance_path)
        result = generate_one_exercise_instance(exercise, instance_path)
        if result["code"] != 0:
            print("Exercise generator failed: exit status %s", result["code"])
            print("Exercise generator stdout: %s", result["out"])
            print("Exercise generator stderr: %s", result["err"])
            raise ExerciseGenerationError("Exercise generator failed: exit status %s\nStderr: %s" % (result["code"], result["err"]))
        index += 1


def generate_one_exercise_instance(exercise, dir_path):
    '''
    Generate one new exercise instance in the given directory.
    '''
    if not ("generator" in exercise and "cmd" in exercise["generator"]):
        raise Exception(
            'Missing "generator" and/or "cmd" under "generator" in the exercise configuration %s' % exercise["key"]
        )

    # Default cwd is the course directory
    cwd = os.path.dirname(os.path.abspath(__file__))
    if "cwd" in exercise["generator"]:
        # If cwd is set, it should reside inside course directory
        cwd = os.path.join(cwd, exercise["generator"]["cwd"])

    command = exercise["generator"]["cmd"][:] # Copy the command list from config before appending
    command.append(dir_path)
    return invoke(command, cwd)


def invoke(cmd_list, cwd=None):
    '''
    Invokes a shell command.

    @type cmd_list: C{list}
    @param cmd_list: command line arguments
    @type cwd: C{str}
    @param cwd: set current working directory for the command, None if not used
    @rtype: C{dict}
    @return: code = process return code, out = standard out, err = standard error
    '''
    p = subprocess.Popen(cmd_list, universal_newlines=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    out, err = p.communicate()
    return {"code": p.returncode, "out": out.strip(), "err": err.strip()}


def parse_config(path):
    '''
    Parses a dict from a file.

    @type path: C{str}
    @param path: a path to a file
    @type loader: C{function}
    @param loader: a configuration file stream parser
    @rtype: C{dict}
    @return: an object representing the configuration file or None
    '''
    formats = {
        'json': json.load,
        'yaml': yaml.safe_load
    }
    try:
        loader = formats[os.path.splitext(path)[1][1:]]
    except:
        raise Exception('Unsupported format "%s"' % (path))
    data = None
    with open(path) as f:
        try:
            data = loader(f)
        except (ValueError, yaml.YAMLError) as e:
            raise Exception("Configuration error in %s" % (path), e)
    return data


def parse_rst(path):
    '''
    Parses a list of dicts from a file.

    @type path: C{str}
    @param path: a path to a file
    @rtype: C{list}
    @return: a list representing the found submit-directives
    '''
    file_ext = os.path.splitext(path)[1]
    if file_ext != ".rst":
        raise Exception('Unsupported format "%s"' % (path))
    data = []
    submit_found = False
    key = None
    config = None
    with open(path) as f:
        try:
            for line in f:
                line = line.strip()
                if line.startswith(".. submit::"):
                    parts = re.split("\s+", line)
                    key = parts[2]
                    submit_found = True
                elif line.startswith(":config:") and submit_found:
                    parts = re.split("\s+", line)
                    config = parts[1]
                    data.append({'key': key, 'config': config})
                    submit_found = False
        except IndexError:
            print(f"Failed to parse line '{line}' in file '{path}'.")
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Pregenerate personalized exercise instances"
    )
    # exercise_rst is optional positional argument
    parser.add_argument("exercise_rst", nargs='?', default=None,
            help="Exercise RST file path (relative to this script) containing the submit-directive(s) of "
            "the exercise(s), for which new instances should be generated for. "
            "If the RST file includes multiple submit-directives, you will be asked to confirm personalized "
            "instance generation for each one. By default, all personalized exercises in the course are generated.")
    # Optional arguments
    parser.add_argument("--instances", type=int, default=10, dest="instances",
                        help="Number of instances to generate for an exercise")
    parser.add_argument("--keep-old", action="store_true", dest="keep_old", default=False,
                        help="Keep existing generated instances instead of deleting them first")
    parser.add_argument("--gen-if-none-exist", action="store_true", dest="gen_if_none_exist", default=False,
                        help="Only generate new instances if no instances exist yet")

    args = parser.parse_args()

    exercise_rst = args.exercise_rst

    all_rst_files = []
    if exercise_rst:
        all_rst_files.append(exercise_rst)
    else:
        for root, dirs, files in os.walk('.'):
            for filename in files:
                if filename.endswith(".rst"):
                    all_rst_files.append(os.path.join(root, filename))
    if not all_rst_files:
        print("The course has no personalized exercises so no instances are generated.")
        exit()

    all_keys_and_exercises = []
    for rst_file in all_rst_files:
        rst_data = parse_rst(rst_file)
        for data in rst_data:
            exercise_config = data['config']
            exercise_key = data['key']
            exercise = parse_config(exercise_config)
            if exercise is None:
                raise Exception("Exercise config not found: %s" % exercise_config)
            if "personalized" in exercise and exercise["personalized"]:
                exercise['key'] = '_'.join(
                    part for part in os.path.splitext(rst_file)[0].split('/') if part not in ['.', '..']
                    ) + '_' + exercise_key
                all_keys_and_exercises.append({'key': exercise_key, 'exercise': exercise})

    print("Found personalized exercises with the following keys:")
    for data in all_keys_and_exercises:
        print(data['key'])
    print()

    exercises = []
    confirm_all = False
    for data in all_keys_and_exercises:
        confirm_string = None
        if not confirm_all:
            confirm_string = input(
                f"Include personalized exercise with the key '{data['key']}'? "
                "Yes(Y) / No(N) / Yes to all(A) / Cancel(C) "
            ).strip().lower()
        if confirm_string == 'a':
            confirm_all = True
        if confirm_all or confirm_string == 'y':
            exercises.append(data['exercise'])
        elif confirm_string == 'c':
            print("Cancelled.")
            exit()
        elif confirm_string != 'n':
            raise Exception(f"Invalid input '{confirm_string}'")
    print()

    # Exercises have been parsed
    if args.instances < 1:
        raise Exception("--instances value must be at least 1")

    for ex in exercises:
        if args.gen_if_none_exist and pregenerated_exercise_instances(ex):
            # Some instances already exist so do not delete them and do not generate any new instances
            continue

        if not args.keep_old:
            delete_pregenerated_exercise_instances(ex)

        # Ensure that base directory exists
        prepare_pregenerated_exercises_directory(ex)
        generate_exercise_instances(ex, args.instances)

    print("Personalized exercises generated!")
