from .base_page import BasePage
from .lokators import MainPageLocators

class MainPageGoogle(BasePage):

    def should_be_all_elements_present(self):
        self.should_be_search_area()
        self.should_be_google_search_button()
        self.should_be_lucky_button()
        self.should_be_enter_button()
        self.should_be_google_image()
        self.should_be_change_language_area()


    def should_be_search_area(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_LINE), 'Search area is not presented'

    def should_be_google_search_button(self):
        assert self.is_element_present(*MainPageLocators.GOOGLE_SEARCH_BUTTON), 'Search button is not presented'

    def should_be_lucky_button(self):
        assert self.is_element_present(*MainPageLocators.LUCKY_BUTTON), 'Lucky button is not presented'

    def should_be_enter_button(self):
        assert self.is_element_present(*MainPageLocators.ENTER_BUTTON), 'Enter button is not presented'

    def should_be_google_image(self):
        assert self.is_element_present(*MainPageLocators.GOOGLE_IMAGE), 'Google image is not presented'

    def should_be_change_language_area(self):
        assert self.is_element_present(*MainPageLocators.CHANGE_LANGUAGE_AREA), 'Change language area is not presented'

    text = 'Search somthing'

    def search_text(self, text):

        self.browser.find_element(*MainPageLocators.SEARCH_LINE).send_keys(text)
        self.browser.find_element(*MainPageLocators.GOOGLE_SEARCH_BUTTON).click()

    def searching_text_should_be_on_result_page(self, text):
        assert text in self.browser.page_source, 'Search does not work'

    def search_in_url(self, text):
        assert text in self.browser.current_url, 'text is not in url'

