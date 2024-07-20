import pytest
from selenium import webdriver



@pytest.fixture(scope="class")
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.get("https://react-ts-redux-realworld-example-app.netlify.app/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
