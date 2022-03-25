from mpc_training import team
import pytest
import math

input_expected=[(0, '0.00'), (1, '30.07'), (2, '47.73'), (3, '62.55'),
                (4, '75.77'), (5, '87.93'), (6, '99.29'), (7, '110.04'),
                (8, '120.28'), (9, '130.11')]
@pytest.mark.parametrize("input_int,expected_output", input_expected)
def test_mikea(input_int, expected_output):
    start_string = f"The {input_int}:1 Mean-Motion-Resonance with Neptune is at"
    assert team.mpc_mikea(input_int).startswith(start_string)
    print(team.mpc_mikea(input_int).split()[-2])
    assert team.mpc_mikea(input_int).split()[-2] == expected_output
