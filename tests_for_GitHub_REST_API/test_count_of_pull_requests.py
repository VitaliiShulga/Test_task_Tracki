from selenium import webdriver
import requests

def count_open_pulls():
    username = 'Fantomas42'
    repo = 'django-blog-zinnia'
    count_open = 0
    url_open = f'https://api.github.com/repos/{username}/{repo}/pulls?state=open'
    open_data = requests.get(url_open).json()

    for request in open_data:
        for key, value in request.items():
            if key == 'state' and value == 'open':
                count_open += 1
    return count_open

def count_closed_pulls():
    username = 'Fantomas42'
    repo = 'django-blog-zinnia'
    count_close = 0
    url = f'https://api.github.com/repos/{username}/{repo}/pulls?state=closed&per_page=100&page=1'
    data = requests.get(url).json()

    for request in data:
        for key, value in request.items():
            if key == 'state' and value == 'closed':
                count_close += 1

    url = f'https://api.github.com/repos/{username}/{repo}/pulls?state=closed&per_page=100&page=2'
    data = requests.get(url).json()

    for request in data:
        for key, value in request.items():
            if key == 'state' and value == 'closed':
                count_close += 1

    return count_close



class TestsCountsPullRequests:
    def test_status_code(self):
        username = 'Fantomas42'
        repo = 'django-blog-zinnia'
        url = f'https://api.github.com/repos/{username}/{repo}/pulls'
        status = requests.get(url).status_code
        assert status == 200, f"Status code = {status} it is not 200"

    def test_count_of_open_pull_requests(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://github.com/Fantomas42/django-blog-zinnia/pulls')
        open = self.driver.find_element_by_xpath('//a [@class="btn-link selected"]')
        open = open.text.split()[0]
        assert int(open) == count_open_pulls(), f'count open pull in web == {int(open)} this != {count_open_pulls()}'
        self.driver.close()

    def test_count_of_closed_pull_requests(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://github.com/Fantomas42/django-blog-zinnia/pulls')
        closed = self.driver.find_element_by_xpath('//a [@class="btn-link "]')
        closed = closed.text.split()[0]
        assert int(closed) == count_closed_pulls(), f'count closed pull in web == {int(closed)} this != {count_closed_pulls()}'
        self.driver.close()

