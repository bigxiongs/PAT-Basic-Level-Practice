import unittest

class Solution():
    def convertion(self, num):
        status = 0
        res = ""
        if num < 100:
            status = 1
        if num < 10:
            status = 2
        if status == 0:
            for i in range(num // 100):
                res = res + "B"
            status = 1
        if status == 1:
            for i in range(num // 10 % 10):
                res = res + "S"
            status = 2
        if status == 2:
            for i in range(num % 10):
                res = res + str(i + 1)
        return res

class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().convertion(234), "BBSSS1234")
        self.assertEqual(Solution().convertion(23), "SS123")

if __name__ == '__main__':
    unittest.main()