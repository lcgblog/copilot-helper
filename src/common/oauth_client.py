import requests
from requests.auth import HTTPBasicAuth

class OAuth2Client:
    def __init__(self, client_id, client_secret, token_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.access_token = None

    def get_access_token(self):
        if not self.access_token:
            response = requests.post(
                self.token_url,
                auth=HTTPBasicAuth(self.client_id, self.client_secret),
                data={'grant_type': 'client_credentials'}
            )
            if response.status_code == 200:
                self.access_token = response.json().get('access_token')
            else:
                raise Exception('Failed to retrieve access token')

        return self.access_token

    def call_api(self, api_url):
        headers = {'Authorization': f'Bearer {self.get_access_token()}'}
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('API call failed')