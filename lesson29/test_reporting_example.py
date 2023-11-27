import pytest


def test_check_two_p_two():
    assert 2 + 2 == 4


def test_check_two_m_two():
    assert 2 * 2 == 4


@pytest.mark.skip('we didn`t create this part yet')
def test_skip():
    pass