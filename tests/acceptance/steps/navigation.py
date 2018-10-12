from behave import *
from selenium import webdriver

from acceptanceTesting.tests.acceptance.page_model.blog_page import BlogPage
from acceptanceTesting.tests.acceptance.page_model.home_page import HomePage
from acceptanceTesting.tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/Vladislav_Aks/Desktop/acceptanceTesting/acceptanceTesting/tests/'
                                      'acceptance/steps/chromedriver')
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/Vladislav_Aks/Desktop/acceptanceTesting/acceptanceTesting/tests/'
                                      'acceptance/steps/chromedriver')
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome('/Users/Vladislav_Aks/Desktop/acceptanceTesting/acceptanceTesting/tests/'
                                      'acceptance/steps/chromedriver')
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
