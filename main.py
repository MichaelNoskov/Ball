"""Scrolling Ball"""


def degree(radius: float, acceleration: float, time: float, velocity: float = 0.0) -> float:
    """Calculates the angle of shifting the ball

    :param radius: float
    :param acceleration: float
    :param time: float
    :param velocity: float
    :return: float
    """
    s = velocity * time + acceleration * time ** 2 / 2
    c = 2 * 3.14 * radius
    angle = s % c / (c/360)
    return round(angle, 2)
