import pytest
import random
from quicksort import sort


# Everybody is using py.test anyway

def test_equal_numbers():
    a = 15
    b = 15
    assert a == b
    assert a is b


class TestEqual:
    def test_equal_small_numbers(self):
        a = 150 * 1
        b = 150 * 1
        assert a == b
        assert a is b

    def test_equal_large_numbers(self):
        a = 300 * 1
        b = 300 * 1
        assert a == b
        assert a is not b


# Fixtures !


@pytest.fixture
def rnd():
    return random.random()


@pytest.fixture
def fixture_a(rnd):
    return rnd


@pytest.fixture
def fixture_b(rnd):
    return rnd


def test_fixtures(fixture_a, fixture_b):
    assert fixture_a == fixture_b


# fixture factories
@pytest.fixture()
def get_rand():
    def getter():
        return random.random()
    return getter


@pytest.fixture
def fixt_a(get_rand):
    return get_rand()


@pytest.fixture
def fixt_b(get_rand):
    return get_rand()


def test_fixts(fixt_a, fixt_b):
    assert fixt_a != fixt_b


# # Resoure cleanup == teardown
# @pytest.yield_fixture
# def opened_file():
#     f = open('file.txt')
#     try:
#         yield f
#     finally:
#         f.close()


def test_sort(opened_file):
    raw_array = opened_file.read()  # string
    array = [int(item) for item in raw_array.split(' ')]
    assert sorted(array) == sort(array)

# file factory if we want to send filename


@pytest.mark.parametrize(
    'array', ([5, 4, 3, 2, 1], [1, 1, 1, 1], [66, 55, 33, 99]))
def test_param_sort(array):
    assert sort(array) == sorted(array)



# Fixture Scope
#  - function(default) - run for every test
#  - class - run for every class
#  - module - run for every module
#  - session - run for session only 1 time