import os
import pytest
from dotenv import load_dotenv
from xts_api_client.xts_connect_async import XTSConnect
load_dotenv()

API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")

xt = XTSConnect(
    apiKey = API_key,
    secretKey = API_secret,
    source = API_source,
    root = API_root
)


def test_marketdata_login():
    response = xt.marketdata_login()
    print(response)
    assert response['type'] == 'success'
    
# @pytest.fixture(scope="session", autouse=True)
# def session():
#     response = xt.marketdata_login()
#     assert response['type'] == 'success'
#     yield
#     response = xt.marketdata_logout()
#     assert response['description'] == 'successfully logout.'

# def test_get_config():
#     response_get_config = xt.get_config()
#     assert response_get_config['type'] == 'success'