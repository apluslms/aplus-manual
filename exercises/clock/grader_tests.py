import unittest
import graderunittest
from selenium import webdriver
from datetime import datetime
import time

class TestClock(unittest.TestCase):

    """Selenium tests assessing contents and functionality of JS exercise."""

    @classmethod
    def setUpClass(cls):
        #docker paths
        cls.driver = webdriver.Firefox()
        cls.driver.get('file:///submission/user/clock.html')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def _assert_elements_found(self, elems):
        """Locates elements in html document. Searched elements are given as
        'elems' dictionary, where key indicates the identifier type (e.g. 'tag')
        for element and value indicates the value of identifier (e.g.
        'input')."""

        d = self.__class__.driver
        #Multiple methods to locate elements
        #Requires a policy in e.g. ids used in submissions
        #Also methods for all elements with common identifier,
        #see keys in plural
        methods = {'tag': d.find_element_by_tag_name,
                    'id': d.find_element_by_id,
                    'xpath': d.find_element_by_xpath,
                    'tags': d.find_elements_by_tag_name,
                    'ids': d.find_elements_by_id,
                    'xpaths': d.find_elements_by_xpath
                    }

        for identifier, value in elems.items():
            finder = methods[identifier]
            try:
                found = finder(value)
            except:
                self.assertTrue(False,
                    """Could not find an element with attribute '{}' having
                       value '{}'."""
                       .format(identifier, value)
                )

    def _assert_correct_time(self):
        clockString = None
        i = 0
        while not clockString and i < 20:
            clock = self.__class__.driver.find_element_by_tag_name('h1')
            clockString = clock.text
            i += 1
        self.assertTrue(clockString,
            "Could not find the time in the text contents of tag '{}'."
               .format('h1')
            )
        # Convert to datetime for comparison
        day = str(datetime.now().date())
        try:
            clockTime = datetime.strptime(' '.join([day, clockString]), '%Y-%m-%d %H:%M:%S')
        except:
            self.fail("""The tag '{}' has text contents '{}', which is not in
                         recognizable time format. Use the format 'hh:mm:ss'."""
                        .format('h1', clockString)
                        )
        # Get local time
        localTime = datetime.now()
        diff = abs(localTime - clockTime).total_seconds()
        self.assertTrue(diff <= 2,
            "The time of the clock differs from the expected by {} seconds."
            .format(diff)
            )

    #def _assert_clock_updates(self):
    #    clock = self.__class__.driver.get_element_by_tag_name('h1')


    def _assert_colors_change(self):
        # Check colors change
        # TODO: match them to correct modulo of 2
        # representation of webElement color value
        red = "rgb(255, 0, 0)"
        blue = "rgb(0, 0, 255)"
        colors = []
        i = 0
        while (red not in colors or blue not in colors) and i < 100:
            clockElem = self.__class__.driver.find_element_by_tag_name('h1')
            color = clockElem.value_of_css_property("color")
            if (color == red or color == blue) and color not in colors:
                colors.append(color)
            i += 1
            time.sleep(0.5)

        self.assertTrue(red in colors and blue in colors,
            "Check the colors and how the colors are updated."
            )

    def test_1_elements_found(self):
        """The page contains expected elements. (1p)"""
        self._assert_elements_found({'tag': 'h1',
            })

    def test_2_clock_time(self):
        """The clock has correct time. (1p)"""
        self._assert_correct_time()

    def test_3_colors(self):
        """The colors change as expected. (1p)"""
        self._assert_colors_change()

    def test_4_clock_updates(self):
        """The time updates correctly. (1p)"""
        for _ in range(3):
            time.sleep(1)
            self._assert_correct_time()

if __name__ == '__main__':
    unittest.main(testRunner=graderunittest.PointsTestRunner(verbosity=2))
