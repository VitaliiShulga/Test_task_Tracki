import requests
from jsonschema import validate


def get_branches():
    username = 'Fantomas42'
    repo = 'django-blog-zinnia'
    url = f'https://api.github.com/repos/{username}/{repo}/branches'
    data = requests.get(url).json()
    return data


def validate_response():
    # Describe what kind of json we expect.
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "commit": {
                "type": "object",
                "properties": {
                    "sha": {"type": "string"},
                    "url": {"type": "string"}
                }
            },
            "protected": {"type": "boolean"}
        }
    }
    for response in get_branches():
        validate(response, schema=schema)
    print('\n', get_branches())


# validate_response()


class TestsListOfBranchesAndSchemaOfResponse:
    def test_status_code(self):
        username = 'Fantomas42'
        repo = 'django-blog-zinnia'
        url = f'https://api.github.com/repos/{username}/{repo}/branches'
        status = requests.get(url).status_code
        assert status == 200, f"Status code {status} it is not 200"

    def test_branches_and_schema(self):
        validate_response()



