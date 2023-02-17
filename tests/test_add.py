import pytest

from python_skeleton import add

@pytest.mark.parametrize(('x', 'y', 'expected'), [
    (1,2,3),
    (0,0,0),
])
def test_add(x, y, expected):
    assert add(x,y) == expected
