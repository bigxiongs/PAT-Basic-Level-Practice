import unittest

class Solution():
    def writeTheNum(self, num):
        s = sum([int(n) for n in num])
        numbers = {
            '0': "ling",
            '1': "yi",
            '2': "er",
            '3': "san",
            '4': "si",
            '5': "wu",
            '6': "liu",
            '7': "qi",
            '8': "ba",
            '9': "jiu"
        }
        return " ".join(numbers[n] for n in str(s))

class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().writeTheNum('1234567890987654321123456789'), "yi san wu")

if __name__ == '__main__':
    unittest.main()