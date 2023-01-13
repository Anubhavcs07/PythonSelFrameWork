import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # the path to log file
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        # pass filehandler object to it
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, text)))
