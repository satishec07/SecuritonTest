from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    login = (By.XPATH, "//a[@href='#/login']")
    email = (By.XPATH, "//input[@placeholder='Email']")
    password = (By.XPATH, "//input[@placeholder='Password']")
    submit = (By.XPATH, "//button[text()='Sign in']")
    globalFeed = (By.XPATH, "//a[text()='Global Feed']")
    pagination = (By.XPATH,"//ul[@class='pagination']/li")
    pageNumber = (By.XPATH, "//ul[@class='pagination']/li/a")
    content = (By.XPATH, "//h1")
    heart = (By.XPATH, "//a[contains(@href,'TCP-circuit')]/parent::div//button")
    heartCount = (By.XPATH, "//a[contains(@href,'TCP-circuit')]/parent::div//button/i")


    def getLogin(self):
        return self.driver.find_element(*Login.login)

    def getEmail(self):
        return self.driver.find_element(*Login.email)

    def getPassword(self):
        return self.driver.find_element(*Login.password)

    def getSubmit(self):
        return self.driver.find_element(*Login.submit)

    def getGlobalFeed(self):
        return self.driver.find_element(*Login.globalFeed)

    def getPagination(self):
        return self.driver.find_elements(*Login.pagination)

    def getPageNumber(self):
        return self.driver.find_elements(*Login.pageNumber)

    def getContent(self):
        return self.driver.find_elements(*Login.content)

    def getHeartClick(self):
        return self.driver.find_element(*Login.heart)

    def getHeartCount(self):
        return self.driver.find_element(*Login.heartCount)
