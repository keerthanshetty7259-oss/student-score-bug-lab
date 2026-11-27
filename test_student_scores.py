import unittest

from student_scores import calculate_total, calculate_average, calculate_grade


class StudentScoresTests(unittest.TestCase):
    def test_total_for_basic_scores(self):
        self.assertEqual(calculate_total([10, 20, 30]), 50)

    def test_average_for_basic_scores(self):
        self.assertAlmostEqual(calculate_average([10, 20, 30]), 20.0)

    def test_grade_for_high_score(self):
        self.assertEqual(calculate_grade(95), "A")


if __name__ == "__main__":
    unittest.main()
