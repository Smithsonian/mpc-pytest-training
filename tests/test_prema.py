from mpc_training import team
import pytest
import math


@pytest.mark.parametrize("input_int", range(0, 9))
def test_prema(input_int):
    assert team.mpc_paresh(input_int).startswith("The square root of ")
    assert float(team.mpc_paresh(input_int).split()[-1]) == math.sqrt(input_int)
