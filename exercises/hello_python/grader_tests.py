import unittest
from graderutils import graderunittest
from graderutils.graderunittest import points


class TestHelloPython(unittest.TestCase):

    @points(1)
    def test_import(self):
        """Import the functions module"""
        # If this fails, it indicates the file is not a proper Python
        # program.
        import functions

    @points(1)
    def test_function(self):
        """Check hello function exists"""
        # Does the same as test_import, but also check that the module
        # "functions" defines the name "hello" which refers to a function.
        import functions
        def protofunction():
            pass
        self.assertTrue(type(functions.hello), type(protofunction))

    @points(3)
    def test_return(self):
        """Check hello function return value"""
        # Calls the function "hello" and examines its return value.
        import functions
        self.assertEqual(functions.hello(), "Hello Python!")


if __name__ == '__main__':
    # Run tests from the test case and get result
    loader = unittest.defaultTestLoader
    suite = loader.loadTestsFromTestCase(TestHelloPython)
    runner = graderunittest.PointsTestRunner(verbosity=2)
    result = runner.run(suite)
    # Points are read from stdout and saved
    print("TotalPoints: {}\nMaxPoints: {}".format(result.points, result.max_points))
