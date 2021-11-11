import requests
from pprint import pprint

def get_branches():
    username = 'Fantomas42'
    repo = 'django-blog-zinnia'
    url = f'https://api.github.com/repos/{username}/{repo}/branches'
    data = requests.get(url).json()
    return data

pprint(get_branches())



