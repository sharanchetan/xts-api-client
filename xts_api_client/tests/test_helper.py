import os
import pytest
from dotenv import load_dotenv
from xts_api_client.xts_connect import XTSConnect
import xts_api_client.helper.helper as helper
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


def test_cm_master_string_to_df():
    _cm_master = xt.get_master(exchangeSegmentList=[xt.EXCHANGE_NSECM,xt.EXCHANGE_BSECM])
    cm_master_df = helper.cm_master_string_to_df(_cm_master['result'])
    assert cm_master_df.shape[1] == 22
    assert cm_master_df.shape[0] > 1000


def test_fo_master_string_to_df():
    _fo_master = xt.get_master(exchangeSegmentList=[xt.EXCHANGE_NSEFO,xt.EXCHANGE_BSEFO])
    _fut_df, _opt_df = helper.fo_master_string_to_df(_fo_master['result'])
    assert _fut_df.shape[1] == 21
    assert _fut_df.shape[0] > 1000
    assert _opt_df.shape[1] == 23
    assert _opt_df.shape[0] > 1000