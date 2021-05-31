import unittest
from graderutils import graderunittest
from graderutils.graderunittest import points

class TestHelloPython(unittest.TestCase):

    @points(5)
    def test_return(self):
        """Check hello function return value"""
        # Calls the function "hello" and examines its return value.
        import functions
        self.assertEqual(functions.hello(), "Hello Python!")

if __name__ == '__main__':
    unittest.main(testRunner=graderunittest.PointsTestRunner(verbosity=2))
