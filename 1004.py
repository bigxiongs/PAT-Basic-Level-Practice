import unittest

class Solution():
    def scoreRank(self, *students):
        m = 100
        M = 0
        for student in students:
            if student[2] > M:
                Mstudent = student
                M = Mstudent[2]
            if student[2] < m:
                mstudent = student
                m = mstudent[2]
        return Mstudent[0] +' ' + Mstudent[1], mstudent[0] + ' ' + mstudent[1]

class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().scoreRank(
            ('Joe', 'Math990112', 89), ('Mike', 'CS991301', 100), ('Mary', 'EE990830', 95)), 
            ("Mike CS991301", "Joe Math990112"))

if __name__ == '__main__':
    unittest.main()