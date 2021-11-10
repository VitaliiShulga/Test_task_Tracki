from .pages.main_page_google import MainPageGoogle

def test_elements_is_present(browser):
    link = 'https://www.google.com/'
    page = MainPageGoogle(browser, link)
    page.open()
    page.should_be_search_area()
    page.should_be_google_search_button()
    page.should_be_lucky_button()