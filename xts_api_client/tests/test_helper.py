import os
import pytest
from dotenv import load_dotenv
from xts_api_client.xts_connect import XTSConnect
import xts_api_client.helper.helper as helper
from io import StringIO
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
    

def test_cm_master_df_to_xts_cm_instrument_list():
    _cm_master = xt.get_master(exchangeSegmentList=[xt.EXCHANGE_NSECM,xt.EXCHANGE_NSECM])
    cm_master_df = helper.cm_master_string_to_df(_cm_master['result'])
    cm_instrument_list = helper.cm_master_df_to_xts_cm_instrument_list(cm_master_df=cm_master_df, series_list_to_include=["EQ","BE","BZ","SM","A","B"])
    assert len(cm_instrument_list)>100
    assert type(cm_instrument_list) == list
    
def test_fo_master_df_to_xts_future_instrument_list():
    _fo_master = xt.get_master(exchangeSegmentList=[xt.EXCHANGE_NSEFO,xt.EXCHANGE_BSEFO])
    fo_master_df = helper.fo_master_string_to_df(_fo_master['result'])
    xts_future_instrument_list = helper.fo_master_df_to_xts_future_instrument_list(fo_master_df[0],series_list_to_include = ["FUTIDX","FUTSTK","IF"])
    assert len(xts_future_instrument_list)>100
    assert type(xts_future_instrument_list) == list
    
def test_fo_master_df_to_xts_options_instrument_list():
    _fo_master = xt.get_master(exchangeSegmentList=[xt.EXCHANGE_NSEFO,xt.EXCHANGE_BSEFO])
    fo_master_df = helper.fo_master_string_to_df(_fo_master['result'])
    xts_options_instrument_list = helper.fo_master_df_to_xts_options_instrument_list(fo_master_df[1],series_list_to_include = ["OPTIDX","OPTSTK","IF"])
    assert len(xts_options_instrument_list)>100
    assert type(xts_options_instrument_list) == list
    
    
    
    
    