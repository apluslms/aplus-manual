import unittest

from graderutils.graderunittest import points

import plot_helpers


class Test(unittest.TestCase):
    @points(10)
    def test_all_values_in_band(self):
        """solution.produce returns at least 80 values that are in the range [20, 80]"""
        import solution
        correct_count = 0
        iterations = 100
        figure = plot_helpers.make_base_figure(iterations=iterations)
        for iteration in range(iterations):
            value = solution.produce()
            value_is_in_band = 20 <= value <= 80
            # Add green circle if value is in band, else red
            plot_helpers.add_circle(figure, iteration, value, "green" if value_is_in_band else "red")
            correct_count += value_is_in_band
        # If a TestCase patches itself with a user_data dictionary, graderutils will extract and serialize it into the feedback JSON.
        # The contents of the dictionary can then be accessed in the feedback template
        self.user_data = {"plotScript": plot_helpers.make_html_plot(figure)}
        # Fail the test if we found too few values
        self.assertGreaterEqual(correct_count, 80,
            "Found {} correct values, while 80 is required.".format(correct_count)
        )
