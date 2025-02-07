import os
API_key = os.getenv("API_KEY")
API_secret = os.getenv("API_SECRET")
API_source = os.getenv("API_SOURCE")
API_root = os.getenv("API_URL")
"""""""""""""""""""""""""""""""""""""""
      |DataFrame for Cash Market|
"""""""""""""""""""""""""""""""""""""""
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df
from xts_api_client.helper.helper import ohlc_to_df
import asyncio

async def main():
    xt_market_data = XTSConnect(
    apiKey = API_key,
    secretKey = API_secret,
    source = API_source,
    root = API_root
    )
    responce_login_1 = await xt_market_data.marketdata_login()
    print(f"Loggin In: {responce_login_1}")
    market_data_get_master = await xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM] # Works for BSECM as well.
    )
    print((cm_master_string_to_df(market_data_get_master['result'])))
    marget_data_get_ohlc = await xt_market_data.get_ohlc(
    exchangeSegment = xt_market_data.EXCHANGE_NSECM,
    exchangeInstrumentID = 22,
    startTime = "Feb 06 2025 091500",
    endTime = "Feb 06 2025 133000",
    compressionValue = 60)
    print(ohlc_to_df(marget_data_get_ohlc))

    responce = await xt_market_data.marketdata_logout()
    print(f"Loggin Out: {responce}")

    responce_login_2 = await xt_market_data.marketdata_login()
    print(f"Loggin In Again: {responce_login_2}")
    market_data_get_master = await xt_market_data.get_master(
    exchangeSegmentList = [xt_market_data.EXCHANGE_NSECM] # Works for BSECM as well.
    )
    print((cm_master_string_to_df(market_data_get_master['result'])))
    
    marget_data_get_ohlc = await xt_market_data.get_ohlc(
    exchangeSegment = xt_market_data.EXCHANGE_NSECM,
    exchangeInstrumentID = 22,
    startTime = "Feb 06 2025 091500",
    endTime = "Feb 06 2025 133000",
    compressionValue = 60)
    print(ohlc_to_df(marget_data_get_ohlc))

    # Change the values oh OHLC parameters as required.
if __name__ == "__main__":
    asyncio.run(main())
""""""""""""""""""""""""""""""""""""""""""