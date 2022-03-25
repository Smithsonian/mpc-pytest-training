from mpc_training import team
import pytest
import math


@pytest.mark.parametrize("input_int", range(0, 9))
def test_fede(input_int):
    assert team.mpc_federica(input_int).startswith("The base 2 of ")
    mod = input_int % 2
    assert int(team.mpc_federica(input_int).split()[-1]) == mod

    
