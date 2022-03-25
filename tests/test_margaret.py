from mpc_training import team
import pytest
import math


@pytest.mark.parametrize("input_int", range(0, 9))
def test_margaret(input_int):
    assert team.mpc_margaret(input_int).startswith(str(input_int))
    assert team.mpc_margaret(input_int).endswith(str(input_int)+str(input_int))
