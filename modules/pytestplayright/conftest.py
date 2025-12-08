import pytest


@pytest.fixture()
def setup():
    print("test setup")
    yield
    print("teardown")
