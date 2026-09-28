import pytest


@ pytest.mark.sanity
def test_career_page():
    print('this is career page')

@ pytest.mark.sanity
def test_contact_page():
    print('this is contact page')

@ pytest.mark.smoke
def test_about_us_page():
    print('this is about us page')

@ pytest.mark.smoke
def test_blog_page():
    print('this is blog page')

@ pytest.mark.skip
def test_post_page():
    print('this is post page')

@ pytest.fixture(scope='module')
def news_page():
    print('this is news page')

def test_newsLetter_page(news_page):
    print('this is newsLetter page')

def test_add_page(news_page):
    print('this is add page')

@ pytest.fixture(scope='function')
def linkedin_page():
    print('this is linkedin page')

def test_twitter_page(linkedin_page):
    print('this is twitter page')

def test_fb_page(linkedin_page):
    print('this is fb page')