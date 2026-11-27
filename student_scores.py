''"""Utilities for calculating student scores and grades."""


def calculate_total(scores):
    """Return the sum of all student scores."""
    total = 0
    for score in scores:
        total += score
    return total


def calculate_average(scores):
    """Return the average score."""
    if len(scores) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    total = calculate_total(scores)
    return total / len(scores)


def calculate_grade(score):
    """Return the letter grade based on the score."""
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
