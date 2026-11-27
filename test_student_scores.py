import unittest

from student_scores import calculate_total, calculate_average, calculate_grade


class StudentScoresTests(unittest.TestCase):
    def test_total_for_basic_scores(self):
        # Sum of all elements
        self.assertEqual(calculate_total([10, 20, 30]), 60)

    def test_total_single_element(self):
        self.assertEqual(calculate_total([42]), 42)

    def test_total_empty(self):
        self.assertEqual(calculate_total([]), 0)

    def test_average_for_basic_scores(self):
        self.assertAlmostEqual(calculate_average([10, 20, 30]), 20.0)

    def test_average_single_element(self):
        self.assertEqual(calculate_average([100]), 100.0)

    def test_average_empty_raises(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_grade_for_high_score(self):
        self.assertEqual(calculate_grade(95), "A")

    def test_grade_boundaries(self):
        self.assertEqual(calculate_grade(90), "A")   # lower bound inclusive
        self.assertEqual(calculate_grade(75), "B")
        self.assertEqual(calculate_grade(60), "C")
        self.assertEqual(calculate_grade(40), "D")
        self.assertEqual(calculate_grade(0), "F")

    def test_grade_invalid_scores(self):
        with self.assertRaises(ValueError):
            calculate_grade(-5)
        with self.assertRaises(ValueError):
            calculate_grade(105)

    def test_grade_non_numeric(self):
        with self.assertRaises(TypeError):
            calculate_grade("A")


if __name__ == "__main__":
    unittest.main()
