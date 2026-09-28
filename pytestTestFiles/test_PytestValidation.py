import pytest

@pytest.fixture(scope='module') # if scope=function, then this fixture call first before call test function (all time). this is default scope
                                # if scope=module, then this fixture call first before call first test function. not for other tests
def common_case(): # this is normal function (without test in function name)
    print ('this is a common test case')


def test_first_case(common_case): # this is treated as test function | if a function under fixture passes,
                                         # then that will call before call this test function
    print('this is first test case')


def test_second_case(commonCaseNew):
    print('this is second test case')