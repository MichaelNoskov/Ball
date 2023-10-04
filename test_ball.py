"""A module for testing main degree ball function."""
import pytest

from main import degree

data = [
    ((10.5, 13.5, 13.1), 200.91),
    ((12.1, 4.1, 7), 115.65),
    ((10, 10, 5, 6), 168.08)
]


@pytest.mark.parametrize('angle, expected', data)
def test_degree_ball(angle: float, expected: int) -> None:
    """Test degree function with data.

    Args:
        radius: float, ball radius.
        acceleration: float, acceleration of the ball as it rolls.
        time: float, the time he's been rolling.
        velocity: float, initial speed.

    Asserts:
        Float angle of shifting the ball.
    """
    assert degree(*angle) == expected
