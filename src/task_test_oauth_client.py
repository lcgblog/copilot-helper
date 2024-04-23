#!/usr/bin/env python
from common.oauth_client import OAuth2Client
import os

def execute():
    module_name = os.path.basename(__file__)
    print(f"Start testing: {module_name}")
    # Usage example
    client = OAuth2Client(
        client_id='your_client_id',
        client_secret='your_client_secret',
        token_url='https://oauth2.example.com/token'
    )

    api_url = 'https://api.example.com/data'
    data = client.call_api(api_url)
    print(data)
    print(f"End testing: {module_name}")
