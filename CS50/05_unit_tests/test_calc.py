from calculator import square
import pytest

"""
def test_square(): # okay but too tedious
    try:
        assert square(2) == 4
    except AssertionError:
        print("2's square is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3's square is not 9")
    try:
        assert square(-4) == 16
    except AssertionError:
        print("-4's square is not 16")
"""

def test_square_v2():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-4) == 16

def test_str():
    with pytest.raises(TypeError):
        square("cat")