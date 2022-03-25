from mpc_training import team
import pytest
import math


@pytest.mark.parametrize("input_int", range(0, 9))
def test_rosemary(input_int):
    assert team.mpc_rosemary(input_int).startswith("10^")
    assert float(team.mpc_rosemary(input_int).split()[-1]) == 10**(input_int)
