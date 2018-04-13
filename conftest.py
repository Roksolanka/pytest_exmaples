import pytest


# Resoure cleanup == teardown
@pytest.yield_fixture
def opened_file():
    f = open('file.txt')
    try:
        yield f
    finally:
        f.close()
