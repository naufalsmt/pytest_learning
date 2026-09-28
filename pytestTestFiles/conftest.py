import pytest


@pytest.fixture(scope='session')
def commonCaseNew():
    print("this is common new test case")