try:
    # Note! User can tamper with the value and so cheat. Needs a fix in
    # mooc-grader.
    with open('number') as orig_file:
        start = int(orig_file.read().strip())
    with open('solution') as submitted_file:
        solution = int(submitted_file.read().strip())

    max_points = 10
    points = 0
    if solution == (start + 1):
        points = max_points

    print("TotalPoints: {}".format(points))
    print("MaxPoints: {}".format(max_points))

    print("Original number was: {}".format(start))
    print("Your solution was: {}".format(solution))

except Exception:
    print("ERROR")
    raise
