from selenium import webdriver
import requests

count_open = 0
count_close = 0
username = 'Fantomas42'
repo = 'django-blog-zinnia'

url_open = f'https://api.github.com/repos/{username}/{repo}/pulls?state=open'
open_data = requests.get(url_open).json()

for request in open_data:
    for key, value in request.items():
         if key == 'state' and value == 'open':
            count_open += 1

for page_num in range(2):
    url = f'https://api.github.com/repos/{username}/{repo}/pulls?state=closed&per_page=100&page={page_num}'
    data = requests.get(url).json()

    for request in data:
        for key, value in request.items():
            if key == 'state' and value == 'closed':
                count_close += 1

class TestsCountsPullRequests:
    def test_count_of_open_pull_requests(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://github.com/Fantomas42/django-blog-zinnia/pulls')
        open = self.driver.find_element_by_xpath('//a [@class="btn-link selected"]')
        assert int(open.text.split()[0]) == count_open
        self.driver.close()

    def test_count_of_closed_pull_requests(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://github.com/Fantomas42/django-blog-zinnia/pulls')
        closed = self.driver.find_element_by_xpath('//a [@class="btn-link "]')
        closed = closed.text.split()[0]
        assert int(closed) == count_close
        self.driver.close()

