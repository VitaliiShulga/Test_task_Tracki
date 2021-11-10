from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH_LINE = (By.XPATH, '//input [@name="q"]') #/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    GOOGLE_SEARCH_BUTTON = (By.XPATH, '//input [@name="btnK"]')
    LUCKY_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]')