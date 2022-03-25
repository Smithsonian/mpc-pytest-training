from mpc_training import team
import pytest
import numpy as np

data = [    (0,0),
            (1,1),
            (2,4),
            (0.1,0.01),
            ( [0.1],[0.01] ),
            ( [0.1,0.2],[0.01,0.04] ) ,
            ( np.array([0.1,0.3]),np.array([0.01,0.09]) ) ]
@pytest.mark.parametrize("input_val, expected_result", data)
def test_matt(input_val, expected_result):
    assert np.allclose( team.mpc_matt(input_val)[1] , expected_result )

