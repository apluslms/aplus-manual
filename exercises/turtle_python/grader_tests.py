# -*- coding: utf-8 -*-

import unittest
from graderutils.graderunittest import points
import sys
import os
import random
#import canvasvg
import turtles
import model
import simpleturtle
from minipng import Image

class TestTurtle(unittest.TestCase):
    @points(40)
    def test1_get_direction(self):
        """Function get_direction returns string 'right' or 'left' according to specification."""
        count = 200
        for _ in range(count):
            n = random.randint(1, 4096)
            returned_answer = turtles.get_direction(n)
            expected_answer = model.get_direction(n)
            self.assertEqual(
                returned_answer,
                expected_answer,
                "When calling get_direction({0}), your function returned '{1}' when it should return '{2}'."
                .format(n, returned_answer, expected_answer)
            )

    @points(60)
    def test1_2_run_turtles_with_image(self):
        """Function turtles draws the picture without error messages."""
        t = simpleturtle.Turtle()
        turtles.turtles(t)

        t.get_image().write_to_file('turtles.png.base64', 'base64')



if __name__ in ("__main__", "tests"):
    from sys import version_info
    if version_info.major < 3:
        raise Exception("The test were tried to run with Python {:d}.{:d}. Please use version 3.".format(version_info.major, version_info.minor))
    else:
        unittest.main(verbosity=2)
