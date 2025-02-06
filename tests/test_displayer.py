import unittest
from sample import Displayer

class TestDisplayer(unittest.TestCase):
    def setUp(self):
        self.displayer = Displayer("linktosomething")
    def test_missing_init_param_returns_exception(self):
        with self.assertRaises(Exception):
            Displayer()
        

if __name__ == '__main__':
    unittest.main()
