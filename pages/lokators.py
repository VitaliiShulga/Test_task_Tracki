from selenium.webdriver.common.by import By

class MainPageLocators:
    SEARCH_LINE = (By.XPATH, '//input [@name="q"]') #/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    GOOGLE_SEARCH_BUTTON = (By.XPATH, '//input [@name="btnK"]')
    LUCKY_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]')

    ENTER_BUTTON = (By.XPATH, '//a [@class ="gb_3 gb_4 gb_3d gb_3c"]')
    GOOGLE_IMAGE = (By.XPATH, '//img [@class ="lnXdpd"]')
    CHANGE_LANGUAGE_AREA = (By.ID, 'SIvCob')