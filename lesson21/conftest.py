import pytest

from lesson20.pytest_example.cat import Cat

@pytest.fixture
def cat():
    print('we`re in fixture func')
    yield Cat('a','black',0,'street')


@pytest.fixture
def cat2():
    yield Cat('b','white',0,'street')