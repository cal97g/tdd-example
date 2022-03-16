import pytest
from bpcalculate import add

@pytest.mark.parametrize(
    "num_a, num_b,expected",
    [
        (3, 5, 8),
        (2, 4, 6),
        (6, 9, 15),
        (12.3, 12.3, 24.6),
        (30, 30.0, 60.0)
    ]
)
def test_add(num_a, num_b, expected)
    assert add(num_a, num_b) == expected
