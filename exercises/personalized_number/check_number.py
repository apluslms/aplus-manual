import sys

max_points = 10
points = 0
try:
    with open('number') as orig_file:
        # the file from the generated personalized exercise instance
        start = int(orig_file.read().strip())
    with open('solution') as submitted_file:
        # student's submission
        solution = int(submitted_file.read().strip())

    if solution == (start + 1):
        # correct solution
        points = max_points

    print("Original number was: {}".format(start))
    print("Your solution was: {}".format(solution))

except Exception as e:
    print("ERROR", file=sys.stderr)
    print(e, file=sys.stderr)
finally:
    print("TotalPoints: {}".format(points))
    print("MaxPoints: {}".format(max_points))
