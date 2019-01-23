import sys
import solution # student's submission

max_points = 10
points = 0
try:
    answer = solution.hello()

    # it is easy to cheat a simple grader like this one if the student's code
    # is able to read the name file, hence the sandbox should prevent I/O operations
    with open("name", "r") as f:
        # generated personalized instance file
        word = f.read().strip()
    correct_answer = "Hello, {0}!".format(word)

    if answer == correct_answer:
        points = max_points

    print("Your hello function returned: {}".format(answer))
    print("The correct answer is: {}".format(correct_answer))

except Exception as e:
    print("ERROR:", file=sys.stderr)
    print(e, file=sys.stderr)
finally:
    print("TotalPoints: {}".format(points))
    print("MaxPoints: {}".format(max_points))

