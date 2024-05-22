import unittest
import Grader


class MyTestCase(unittest.TestCase):
    def test_check_all(self):
        marks = Grader.Marks(95, 90, 100, 99, 70)
        student = Grader.Student('Neel', 10, 'B', marks)
        total = student.marks.total
        percent = student.marks.percent
        result = student.calc_result()
        highest = student.calc_highest()
        self.assertEqual(total, 454)  # add assertion here
        self.assertEqual(percent, 90.8)
        self.assertEqual(result, 'Pass')
        self.assertEqual(highest, 'Math')

    def test_check_fail(self):
        marks = Grader.Marks(28, 31, 40, 2, 3)
        student = Grader.Student('Neel', 10, 'B', marks)
        result = student.calc_result()
        self.assertEqual(result, 'Fail')

    def test_check_pass(self):
        marks = Grader.Marks(35, 37, 32, 34, 35)
        student = Grader.Student('Neel', 10, 'B', marks)
        result = student.calc_result()
        self.assertEqual(result, 'Pass')


if __name__ == '__main__':
    unittest.main

