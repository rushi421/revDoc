from selenium import webdriver
import pytest
import configparser

@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(20)
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI command
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # This will return the browser value to set up method
    return request.config.getoption('--browser')


###########################PyTest HTML Report############################
config = configparser.ConfigParser
"""def pytest_configure(config):
    config._metadata = {
        "Tester": "Rushi",
        "Project Name": "RevDoc",
    }"""

if not hasattr(config, "_metadata"):
    config._metadata = {
        "Tester": "Rushi",
        "Project Name": "RevDoc",
    }
#def pytest_configure(config):  # hook for adding environment info to html report
    """config._metadata['Project Name'] = 'RevDoc'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Rushi'"""


"""@pytest.mark.optionalhook()
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)"""