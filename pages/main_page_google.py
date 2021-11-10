from .base_page import BasePage
from .lokators import MainPageLocators

class MainPageGoogle(BasePage):

    def should_be_all_elements(self):
        self.should_be_search_area()
        self.should_be_google_search_button()
        self.should_be_lucky_button()


    def should_be_search_area(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_LINE), 'Search area is not presented'

    def should_be_google_search_button(self):
        assert self.is_element_present(*MainPageLocators.GOOGLE_SEARCH_BUTTON), 'Search button is not presented'

    def should_be_lucky_button(self):
        assert self.is_element_present(*MainPageLocators.LUCKY_BUTTON), 'Lucky button is not presented'

