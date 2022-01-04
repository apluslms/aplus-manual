import unittest
import random

from graderutils.graderunittest import points
from graderutils.iotester import IOTester, ENTER


# Name of the Python module that is going to be tested
module_to_test = "dice"

# Create an instance of IOTester with default settings, except for ignored_characters.
# The default settings of IOTester ignore missing/extra periods, but in this exercise we want to
# make sure that the student prints a period after every roll, like in the table below:
# ----------------------
# Roll    Die 1    Die 2
# ----------------------
# 1.      2        5
# 2.      1        3
# ----------------------
iotester = IOTester(settings={"ignored_characters": [',', '!', '?', ':', ';', '\'']})

# Define argument lists that are going to be used in the tests
args_init_dice = [
    [1234],
    [465],
    [random.randint(100, 5000)],
]

args_roll_dice_once = [
    [1],
    [3],
    [random.randint(5, 9)],
]

args_all_rolls = [
    [
        [ # 2 rolls, 3 dice
            [5, 2, 6],
            [3, 3, 4],
        ],
    ],
    [
        [ # 3 rolls, 2 dice
            [1, 3],
            [2, 6],
            [4, 2],
        ],
    ],
    [
        [ # 4 rolls, 2 dice
            [random.randint(1, 6), random.randint(1, 6)],
            [random.randint(1, 6), random.randint(1, 6)],
            [random.randint(1, 6), random.randint(1, 6)],
            [random.randint(1, 6), random.randint(1, 6)],
        ],
    ],
]

# Define user inputs that are going to be used in the tests
inputs_main = [
    [ # 2 rolls, 3 dice
        510,
        3,
        2,
        ENTER, # Represents the user pressing the Enter key without inputting any characters (equal to string "[iotester-enter]")
    ],
    [ # 3 rolls, 2 dice, random seed
        random.randint(100, 5000),
        2,
        3,
        ENTER,
    ],
    [ # 4-5 rolls, 2-3 dice, random seed
        random.randint(100, 5000),
        random.randint(2, 3),
        random.randint(4, 5),
        ENTER,
    ],
]


class TestCaseDice(unittest.TestCase):

    def setUp(self):
        # Before each test method, prepare the Python module i.e., check for UnicodeDecodeError
        # and SyntaxError in module_to_test, and if main() function exists/is called.
        #
        # A setUp-method should not be used if testing multiple Python modules. In those cases,
        # call prepare in the beginning of each test method with the corresponding module name.
        iotester.prepare(self, module_to_test)


    def tearDown(self):
        # After running a test method, restore IOTester state and clean up possible files created.
        # Do not forget this, otherwise weird things might happen.
        iotester.restore()

    # In this exercise the maximum amount of points is set to 100 in the exercise RST file,
    # so we make sure that all the points from each test method add up to 100.

    @points(10)
    def test_01_init_dice(self):
        """Test function 'init_dice'"""
        description1 = "Checking that you don't print anything\nin function 'init_dice'."
        description2 = "Checking that you correctly initialize the\npseudo-random number generator."
        for args in args_init_dice:
            iotester.no_output_test(func_name="init_dice", args=args, desc=description1)
            iotester.random_state_test(func_name="init_dice", args=args, desc=description2)


    @points(15)
    def test_02_roll_dice_once(self):
        """Test function 'roll_dice_once'"""
        description1 = "Checking that you don't print anything\nin function 'roll_dice_once'."
        description2 = "Checking that you only generate the needed amount of\npseudo-random numbers."
        for args in args_roll_dice_once:
            iotester.no_output_test(func_name="roll_dice_once", args=args, desc=description1)
            iotester.random_state_test(func_name="roll_dice_once", args=args, desc=description2)
            iotester.return_value_test(func_name="roll_dice_once", args=args)


    @points(15)
    def test_03_print_results_text_and_numbers(self):
        """Test text and numbers in the output of function 'print_results'"""
        # This test will pass if the student program's output has correct text and numbers.
        # Mistakes in whitespace (spaces and line breaks) do not cause this test to fail.
        for args in args_all_rolls:
            iotester.text_test(func_name="print_results", args=args)
            iotester.numbers_test(func_name="print_results", args=args, compare_formatting=True)


    @points(10)
    def test_04_print_results_whitespace(self):
        """Test whitespace in the output of function 'print_results'"""
        # This test will only pass if the student program's output has correct text,
        # numbers AND whitespace.
        for args in args_all_rolls:
            iotester.complete_output_test(func_name="print_results", args=args)


    @points(15)
    def test_05_save_results(self):
        """Test function 'save_results'"""
        description = "Checking that you don't print anything\nin function 'save_results'."
        for args in args_all_rolls:
            iotester.no_output_test(func_name="save_results", args=args, desc=description)
            # Check that the results.csv file created by the student program is identical to
            # the file created by the model program:
            iotester.created_file_test(file_name="results.csv", func_name="save_results", args=args)


    @points(25)
    def test_06_main(self):
        """Test function 'main'"""
        description = (
            "Checking that you correctly initialize the\npseudo-random number generator "
            "and only generate the\nneeded amount of pseudo-random numbers."
        )
        # In this test, inputs are fed to the two programs as if a user was inputting them using
        # a keyboard.
        for inputs in inputs_main:
            iotester.random_state_test(func_name="main", inputs=inputs, desc=description)
            iotester.complete_output_test(func_name="main", inputs=inputs)
            iotester.created_file_test(file_name="results.csv", func_name="main", inputs=inputs)


    @points(10)
    def test_07_amount_of_functions(self):
        """Test the amount of functions you have defined"""
        # Check that the student has defined exactly five functions:
        iotester.amount_of_functions_test(op="==", amount=5)
