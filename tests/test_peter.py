from mpc_training import team
import pytest
import math


@pytest.mark.parametrize("a",range(0, 9))
def test_peter(a):
    assert team.mpc_peter(a)
    assert float(team.mpc_peter(a)) == a**3-10
