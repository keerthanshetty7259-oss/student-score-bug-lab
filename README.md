# Student Score Bug Lab

A tiny Python project that calculates student totals, averages, and letter grades.
It is intentionally provided as a debugging exercise.

## Files

- `student_scores.py` — score calculation functions.
- `test_student_scores.py` — a small starter test suite.

## Expected behavior

- `calculate_total(scores)` should add every score in the list.
- `calculate_average(scores)` should calculate the arithmetic mean of every score.
  An empty list should raise `ValueError`.
- `calculate_grade(score)` should use these boundaries:

| Score | Grade |
|---|---|
| 90–100 | A |
| 75–89 | B |
| 60–74 | C |
| 40–59 | D |
| 0–39 | F |

Scores are expected to be numeric values between 0 and 100.

## Run

```bash
python -m unittest -v
```

## Debugging exercise

Investigate the implementation, identify incorrect results and edge cases, fix the
underlying problems, and add unit tests for the expected behavior.
