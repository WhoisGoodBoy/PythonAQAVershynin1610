import pytest
from lesson20.pytest_example.cat import Cat

def test_cat_aging():
    cat = Cat('falalfel','brown',2,'manul')
    cat.grow()
    assert cat.age == 3


@pytest.mark.xfail(reason='failed due to known bug')
def test_cat_renamed(cat):
    cat.name = 'falafel23'
    assert cat.name == 'falafel2'

@pytest.mark.skip('skipped becuase this part of product unfinished')
def test_cat_renamed_another_way(cat2):
    cat2.name = 'falafel2'
    assert cat2.name == 'falafel23'

@pytest.mark.regression
def test_cat_renamed3(cat):
    cat.name = 'falafel23'
    assert cat.name == 'falafel2'

@pytest.mark.regression
@pytest.mark.smoke
def test_cat_aging2():
    cat = Cat('falalfel','brown',2,'manul')
    cat.grow()
    assert cat.age == 3


@pytest.mark.parametrize(
    'name_given,name_expected', [('murchyk', 'murchyk'), ('patron','patron'), ('catname', 'dogname')]
)
def test_cat_renamed_with_params(cat2, name_given, name_expected):
    cat2.name = name_given
    if name_given == 'catname':
        assert cat2.name == 'catname'
    else:
        assert cat2.name == name_expected
