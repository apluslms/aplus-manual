import unittest
from graderutils.graderunittest import points

class Test(unittest.TestCase):
    @points(1)
    def test_01(self):
        """Test 1"""
        # Test without user data
        self.assertTrue(True)

    @points(1)
    def test_02(self):
        """Test 2"""
        # Test without user data
        self.assertTrue(False)

    @points(1)
    def test_03(self):
        """Test 3"""
        # Test cases can be patched with a user_data attribute that should be a JSON serializable dict
        self.user_data = {
            "raw_html": "list of things: <ul>" + "\n".join("<li>{}</li>".format(i) for i in range(10)) + "</ul>",
            "preformatted_feedback": """    - preformatted output

            so much whitespace
        hello-
        yellow
        100001"""
        }
        self.assertTrue(False)
