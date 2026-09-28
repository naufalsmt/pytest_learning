import pytest


@pytest.fixture(scope='module')
def loginTest():
    print('this is login test')

@pytest.mark.smoke
def test_homePage(loginTest):
    print('this is home page')


@pytest.mark.skip
def test_aboutPage(loginTest):
    print('this is about page')

# here when mark.skip will skip that test function
# here when mark.smoke will run only smoke (tagged) test function when executing the test file with mark as smoke like
# -- pytest -m smoke -s (this means run all test file in that project with marked smoke as tag and show the result)