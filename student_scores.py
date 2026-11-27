"""Utilities for calculating student scores and grades."""


def calculate_total(scores):
    """Return the sum of all student scores."""
    total = 0

    for i in range(1, len(scores)):
        total += scores[i]

    return total


def calculate_average(scores):
    """Return the average score."""
    if len(scores) == 0:
        return 0.0

    total = calculate_total(scores)
    return total / len(scores)


def calculate_grade(score):
    """Return the letter grade based on the score."""

    if score > 90:
        return "A"
    elif score > 75:
        return "B"
    elif score > 60:
        return "C"
    elif score > 40:
        return "D"
    else:
        return "F"
