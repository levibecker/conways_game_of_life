import unittest
from run import increment

class TestRun(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(1), 2)
        self.assertEqual(increment(-5), -4)

    def test_type_check(self):
        alert_string = 'you can only increment whole numbers!'
        self.assertEqual(increment(1.4), alert_string)
        self.assertEqual(increment('foo'), alert_string)
        self.assertEqual(increment([]), alert_string)
        self.assertEqual(increment(None), alert_string)

if __name__ == '__main__':
    unittest.main()
