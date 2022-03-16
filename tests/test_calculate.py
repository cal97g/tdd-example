import pytest
from bpcalculate import add

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 5, 8),
        (2, 4, 6),
        (6, 9, 15),
        (12.3, 12.3, 24.6),
        (30, 30.0, 60.0)
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1,1,1),
        (1,2,2),
        (1.0, 10.0, 10),
        (10, 10, 100),
        (100, 0, 0),
        (100, 1.5, 150),
        (100, 0.5, 50),
    ]
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
