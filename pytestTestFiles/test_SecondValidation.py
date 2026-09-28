
def test_third_test(commonCaseNew): # declare this fixture function and we can use it on other test functions
    print ('this is a third test case')

# if any fixture found on the same file, it, consider that first, if not it consider from conftest.py file
# if scope=function means, this fixture call every time before run each test function
# if scope=module means, this fixture call only once before the first test function in the same file
# if scope=session means, this fixture call once from the entire session (if run all test together)