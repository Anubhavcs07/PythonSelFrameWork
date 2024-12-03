import logging

import pytest
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxoptions
from selenium import webdriver

from Base.Base import BaseClass
from Base.config import Config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser to use")

@pytest.fixture(scope="class")
def setup(request):
    global driver
    logger = BaseClass.getLogger(__name__)
    base_url = Config.BASE_URL
    # browser = request.config.getoption("--browser", default="chrome").lower()
    # if browser == "chrome":
    chrome_options = ChromeOptions()
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=chrome_options
    )
    logger.info("executing in chrome")
    # elif browser == "firefox":
    #     firefox_options = FireFoxoptions()
    #     # driver = webdriver.Remote(
    #     #     command_executor="http://localhost:4444/wd/hub",
    #     #     options=firefox_options
    #     # )
    #     logger.info("executing on firefox")
    # else:
    #     raise ValueError(f"{browser} is not supported.")

    # service_obj = Service(executable_path=r'C:\Users\sharm\OneDrive\Desktop\Projects\PythonSeleniumProject\Drivers\msedgedriver.exe')
    # driver=webdriver.Edge(service=service_obj)
    # options = Options()
    driver.get(base_url)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
