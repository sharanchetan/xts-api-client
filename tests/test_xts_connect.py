import os
import pytest
from dotenv import load_dotenv
from xts_api_client.xts_connect import XTSConnect
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

@pytest.fixture(scope="session", autouse=True)
def session():
    response = xt.marketdata_login()
    assert response['type'] == 'success'
    yield
    response = xt.marketdata_logout()
    assert response['description'] == 'successfully logout.'

def test_get_config():
    response_get_config = xt.get_config()
    assert response_get_config['type'] == 'success'

def test_get_master():
    response_get_master = xt.get_master(exchangeSegmentList=[xt.EXCHANGE_NSECM])
    assert len(response_get_master['result'].split('NSECM|')) >=1000

def test_get_series():
    response_get_series = xt.get_series(exchangeSegment=1)
    assert 'EQ' in response_get_series['result'], 'Error in getting series'