from .google_com_pages.main_page_google import MainPageGoogle

def test_elements_is_present(browser):
    link = 'https://www.google.com/'
    page = MainPageGoogle(browser, link)
    page.open()
    page.should_be_all_elements_present()

def test_search_is_working(browser):
    link = 'https://www.google.com/'
    text = 'Git'
    page = MainPageGoogle(browser, link)
    page.open()
    page.search_text(text)
    page.search_in_url(text)
    page.searching_text_should_be_on_result_page(text) # try passing "hghghghghgh" to make the test fail