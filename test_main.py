"""A module for testing main degree ball function."""
import pytest

from main import degree

test_data = [
    ((10.5, 13.5, 13.1), 200.91),
    ((12.1, 4.1, 7), 115.65),
    ((10, 10, 5, 6), 168.08),
    ((0, 0, 0, 0), 0),
]


@pytest.mark.parametrize('angle, expected', test_data)
def test_degree_ball(angle: float, expected: float) -> None:
    """Test degree function with data.

    Args:
        angle: float, angle of shifting the ball
        expected: an actual expected degree result.

    Asserts:
        float angle of shifting the ball.
    """
    assert degree(*angle) == expected
