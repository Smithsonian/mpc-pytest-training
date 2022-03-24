from mpc_training import team


def test_chris():
    assert team.chris().startswith("Hi, I'm Chris and today is ")
