import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.loginPage import Login


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_Login(self):
        login = Login(self.driver)
        login.getLogin().click()
        login.getEmail().send_keys("satishec2017@gmail.com")
        login.getPassword().send_keys("Test@123")
        login.getSubmit().click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='Global Feed']")))
        login.getGlobalFeed().click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(4)
        # self.driver.find_element(By.XPATH, "(//ul[@class='pagination']/li/a)[5]").click()
        # textValue_Pagination = self.driver.find_element(By.XPATH, "(//ul[@class='pagination']/li/a)[5]").text
        # print("textValue_Pagination", textValue_Pagination)

        i = 1
        for page in login.getPageNumber():
            i = i + 1
            j = str(i)
            page.find_element(By.XPATH, "//a[normalize-space()='" + j + "']").click()
            time.sleep(2)
            for k in login.getContent():
                if "We need to calculate the wireless TCP circuit" in k.text:
                    print("k.text", k.text)
                    login.getHeartClick()
                    time.sleep(3)





###############################################
        # for k in login.getContent():
        #     i = 1
        #     for page in login.getPageNumber():
        #         j = str(i)
        #         page.find_element(By.XPATH, "//a[normalize-space()='" + j + "']").click()
        #         time.sleep(2)
        #         if "We need to calculate the wireless TCP circuit" in k.text:
        #             print("k.text", k.text)
        #             login.getHeartClick()
        #             hearText = login.getHeartCount().text
        #             print("hearText", hearText)
        #             time.sleep(3)
        #             break
        #         i = i + 1
        #
        #     break
