import os
import unittest


class TumblyCLExists(unittest.TestCase):

    def test_file(self):
        file = os.path.isfile('tumblyCL.py')
        self.assertTrue(file)


if __name__ == '__main__':
    unittest.main()
