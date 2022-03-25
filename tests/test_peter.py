from mpc_training import team
import pytest
import math


@pytest.mark.parametrize("variable_a", "variable_b",range(0, 9),range(0,9))
def test_peter(a,b):
    assert team.mpc_peter(a,b).startswith("random function output is: ")
    assert float(team.mpc_peter(a,b).split()[-1]) == a**3-b**2
