import requests
from requests.auth import HTTPBasicAuth


url = 'https://api.restful-api.dev/objects'

with requests.Session() as session:
    list_of_objects = session.get(url)
    print(list_of_objects.json())

class CRUDWithSession:
    def __init__(self):
        self.session = requests.Session()
        self.url = 'https://api.restful-api.dev/objects'
        self.token = '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'

    def get_an_object(self, object_id):
        return self.session.get(f'{self.url}/{object_id}')

    def get_nonexisting_object(self):
        try:
            response_body = self.get_an_object(-1)
            response_body.raise_for_status()
        except requests.exceptions.HTTPError as err:
            assert err.response.status_code == response_body.status_code

    def get_issues(self):
        headers = {
    "Authorization": f"Bearer {self.token}"
}
        data = {'auth': self.token}
        responce = self.session.get(url='https://api.github.com/octocat',headers=headers)
        resnce2 = self.session.get(url='https://api.github.com/octocat/user/starred/WhoisGoodBoy/tests_for_testing', headers=headers)
        return resnce2


    def mocked_login(self):
        data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
        succesful_login_body = self.session.post(url='https://reqres.in/api/login', data = data)
        return succesful_login_body

    def mocked_login2(self):
        auth = HTTPBasicAuth(password='cityslicka', username='eve.holt@reqres.in')
        succesful_login_body = self.session.post(url='https://reqres.in/api/login', auth=('eve.holt@reqres.in','cityslicka'))
        return succesful_login_body


