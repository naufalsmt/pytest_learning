import pytest


@pytest.fixture(scope='module')
def generalFunction():
    print('this is general test')
    return "this is general function output" # saving this string to generalFunction method


@pytest.fixture(scope='function')
def secondGeneralFunction():
    print('this is second general test')
    yield
    print('this is post second general function test after yield')

def test_firstGeneralFunction(generalFunction):
    print('this is first general test')
    assert generalFunction == 'this is general function output' # validate the return value in generalFunction


def test_secondGeneralFunction(generalFunction, secondGeneralFunction):
    print('this is second general function test')

# yield will pass -- call fixture test or pre yield codes then skip to test function to execute the test function code
# once completed the test function then resume from yield of that fixture 