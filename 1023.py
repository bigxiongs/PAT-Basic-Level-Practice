import unittest

def callatz(a):
    if a == 1:
        return 0
    if a % 2 == 0:
        return 1 + callatz(a // 2)
    return callatz(a * 3 + 1)

class callatzTestCase(unittest.TestCase):
    def test_callatz(self):
        self.assertEqual(callatz(3), 5)

if __name__ == '__main__':
    unittest.main()