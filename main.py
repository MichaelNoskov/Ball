"""Scrolling Ball."""
from math import pi


def degree(radius: float, acceleration: float, time: float, velocity: float = 0) -> float:
    """Calculate the angle of shifting the ball.

    Args:
        radius: float, ball radius.
        acceleration: float, acceleration of the ball as it rolls.
        time: float, the time he's been rolling.
        velocity: float, initial speed.

    Returns:
        Float angle of shifting the ball.
    """
    if radius == 0:
        return 0
    circle = 360
    road = velocity * time + acceleration * time ** 2 / 2
    ball_len = 2 * pi * radius
    angle = road % ball_len / (ball_len/circle)
    return round(angle, 2)
