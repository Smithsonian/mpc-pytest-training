from mpc_training import team
import pytest
import math


@pytest.mark.parametrize("input_int", range(0, 9))
def test_n(input_int):
    result = team.mpc_n(input_int)
    assert result.startswith("<div")
    assert str(input_int) in result
