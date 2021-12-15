import unittest

class Solution():
    def iWantPass(self, s):
        # 字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
        # 任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
        # 如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
        if len(s) < 3:
            return False
        a, b, c = 0, 0, 0
        status = 0
        for char in s:
            if status == 0:
                if char == 'A':
                    a = a + 1
                elif char == 'P':
                    status = 1
                else:
                    return False
            elif status == 1:
                if char == 'A':
                    b = b + 1
                elif char == 'T':
                    status = 2
                else:
                    return False
            else:
                if char == 'A':
                    c = c + 1
                else:
                    return False
        if b == 0:
            return False
        return a + (b - 1) * a == c

class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertTrue(Solution().iWantPass("PAT"))
        self.assertTrue(Solution().iWantPass("PAAT"))
        self.assertTrue(Solution().iWantPass("AAPATAA"))
        self.assertTrue(Solution().iWantPass("AAPAATAAAA"))
        self.assertFalse(Solution().iWantPass("xPATx"))
        self.assertFalse(Solution().iWantPass("PT"))
        self.assertFalse(Solution().iWantPass("Whatever"))
        self.assertFalse(Solution().iWantPass("APAAATAA"))
        self.assertFalse(Solution().iWantPass("APT"))
        self.assertFalse(Solution().iWantPass("APATTAA"))

if __name__ == '__main__':
    unittest.main()