import pandas as pd
from xts_api_client.helper.helper_classes import xts_cm_Instrument,xts_future_Instrument,xts_options_Instrument
from typing import List
from io import StringIO
from decimal import Decimal
from datetime import datetime, timezone, timedelta
import pytz
from xts_api_client.xts_connect_async import XTSConnect

def cm_master_string_to_df(cm_master_result: str) -> pd.DataFrame:
    """
    Converts the response of cm_master API to a pandas DataFrame.
    
    This function takes a string response from the cm_master API, which contains data separated by the '|' character,
    and converts it into a pandas DataFrame. The DataFrame will have predefined column headers.
    
    Parameters:
        cm_master_result (str): The string response from the cm_master API.
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the parsed data from the cm_master_result string.
    """
    col_header = [
        "ExchangeSegment", "ExchangeInstrumentID", "InstrumentType", "Name", "Description", "Series",
        "NameWithSeries", "InstrumentID", "PriceBand_High", "PriceBand_Low", "FreezeQty", "TickSize", "LotSize",
        "Multiplier", "DisplayName", "ISIN", "PriceNumerator", "PriceDenominator", "DetailedDescription",
        "ExtendedSurvlndicator", "Cautionlndicator", "GSMIndicator"
    ]
    _dtype = {
        "ExchangeSegment": str,
        "ExchangeInstrumentID": int,
        "InstrumentType": int,
        "Name": str,
        "Description": str,
        "Series": str,
        "NameWithSeries": str,
        "InstrumentID": int,
        "FreezeQty": int,
        "LotSize": int,
        "Multiplier": int,
        "DisplayName": str,
        "ISIN": str,
        "PriceNumerator": int,
        "PriceDenominator": int,
        "DetailedDescription": str,
        "ExtendedSurvlndicator": int,
        "Cautionlndicator": int,
        "GSMIndicator": int
    }
    _converters = {
            "PriceBand_High": Decimal,
            "PriceBand_Low": Decimal,
            "TickSize": Decimal
        }
    cm_master_df = pd.read_csv(StringIO(cm_master_result), sep = "|",  low_memory =False,header=None,names=col_header,
                            dtype=_dtype,converters=_converters)
    cm_master_df.columns = col_header
    return cm_master_df

from decimal import Decimal
from io import StringIO
import pandas as pd

def fo_master_string_to_df(fo_master_result: str) -> tuple:
    """
    Converts the response of master API to pandas DataFrame for FO segment.
    
    This function takes a string response from the FO master API, splits it into lines, 
    and categorizes each line into futures or options based on the number of columns.
    It then converts these categorized lines into pandas DataFrames with appropriate column headers.
    
    Parameters:
        fo_master_result (str): The string response from the FO master API.
    
    Returns:
        tuple: A tuple containing two pandas DataFrames:
            fut_master_df: DataFrame containing futures data.
            opt_master_df: DataFrame containing options data.
            fur_spread_df: DataFrame containing future spread data.
    """
    opt_col_header = [
        "ExchangeSegment", "ExchangeInstrumentID", "InstrumentType", "Name", "Description", "Series", 
        "NameWithSeries", "InstrumentID", "PriceBand_High", "PriceBand_Low", "FreezeQty", "TickSize", 
        "LotSize", "Multiplier", "UnderlyingInstrumentId", "UnderlyingIndexName", "ContractExpiration", 
        "StrikePrice", "OptionType", "DisplayName", "PriceNumerator", "PriceDenominator", 
        "DetailedDescription"
    ]
    _dtype_opt = {
        "ExchangeSegment": str,
        "ExchangeInstrumentID": int,
        "InstrumentType": int,
        "Name": str,
        "Description": str,
        "Series": str,
        "NameWithSeries": str,
        "InstrumentID": int,
        "FreezeQty": int,
        "LotSize": int,
        "Multiplier": int,
        "UnderlyingInstrumentId": int,
        "UnderlyingIndexName": str,
        "ContractExpiration": str,
        "OptionType": str,
        "DisplayName": str,
        "PriceNumerator": int,
        "PriceDenominator": int,
        "DetailedDescription": str
    }
    
    _converters_opt = {
        "PriceBand_High": Decimal,
        "PriceBand_Low": Decimal,
        "StrikePrice": Decimal,
        "TickSize": Decimal
    }
    
    fut_col_header = [
        "ExchangeSegment", "ExchangeInstrumentID", "InstrumentType", "Name", "Description", "Series", 
        "NameWithSeries", "InstrumentID", "PriceBand_High", "PriceBand_Low", "FreezeQty", "TickSize", 
        "LotSize", "Multiplier", "UnderlyingInstrumentId", "UnderlyingIndexName", "ContractExpiration", 
        "DisplayName", "PriceNumerator", "PriceDenominator", "DetailedDescription"
    ]
    
    _dtype_fut = {
        "ExchangeSegment": str,
        "ExchangeInstrumentID": int,
        "InstrumentType": int,
        "Name": str,
        "Description": str,
        "Series": str,
        "NameWithSeries": str,
        "InstrumentID": int,
        "FreezeQty": int,
        "LotSize": int,
        "Multiplier": int,
        "UnderlyingInstrumentId": int,
        "UnderlyingIndexName": str,
        "ContractExpiration": str,
        "DisplayName": str,
        "PriceNumerator": int,
        "PriceDenominator": int,
        "DetailedDescription": str
    }
    
    _converters_fut = {
        "PriceBand_High": Decimal,
        "PriceBand_Low": Decimal,
        "TickSize": Decimal
    }

    fut_spread_col_header = [
        "ExchangeSegment", "ExchangeInstrumentID", "InstrumentType", "Name", "Description", "Series", 
        "NameWithSeries", "InstrumentID", "PriceBand_High", "PriceBand_Low", "FreezeQty", "TickSize", 
        "LotSize", "Multiplier", "UnderlyingInstrumentId", "UnderlyingIndexName", "ContractExpiration", 
        "DisplayName", "PriceNumerator", "PriceDenominator", "DetailedDescription"
    ]
    
    _dtype_fut_spread = {
        "ExchangeSegment": str,
        "ExchangeInstrumentID": int,
        "InstrumentType": int,
        "Name": str,
        "Description": str,
        "Series": str,
        "NameWithSeries": str,
        "InstrumentID": int,
        "FreezeQty": int,
        "LotSize": int,
        "Multiplier": int,
        "UnderlyingInstrumentId": int,
        "UnderlyingIndexName": str,
        "ContractExpiration": str,
        "DisplayName": str,
        "PriceNumerator": int,
        "PriceDenominator": int,
        "DetailedDescription": str
    }
    
    _converters_fut_spread = {
        "PriceBand_High": Decimal,
        "PriceBand_Low": Decimal,
        "TickSize": Decimal
    }
    
    fut_lines = []
    opt_lines = []
    future_spread_df = []
    rows= fo_master_result.split("\n")
    for row in rows:
        if row.count("|") == 22:
            opt_lines.append(row)
        elif row.count("|") == 20:
            instrumenType = row.split("|")[2]
            if instrumenType=='4':
                future_spread_df.append(row)
            else:
                fut_lines.append(row)
    
    # Join lines back into strings for each category
    fut_string = "\n".join(fut_lines)
    opt_string = "\n".join(opt_lines)
    fut_spread_string = "\n".join(future_spread_df)
    
    # Read Futures DataFrame
    fut_master_df = pd.read_csv(
        StringIO(fut_string), 
        sep="|", 
        low_memory=False, 
        names=fut_col_header,
        dtype=_dtype_fut,
        converters=_converters_fut
    )
    
    # Read Options DataFrame
    opt_master_df = pd.read_csv(
        StringIO(opt_string), 
        sep="|", 
        low_memory=False, 
        names=opt_col_header,
        dtype=_dtype_opt,
        converters=_converters_opt
    )

    # Read Future Spread DataFrame
    fut_spread_df = pd.read_csv(
        StringIO(fut_spread_string), 
        sep="|", 
        low_memory=False, 
        names=fut_spread_col_header,
        dtype=_dtype_fut_spread,
        converters=_converters_fut_spread
    )

    return fut_master_df, opt_master_df, fut_spread_df


def cm_master_df_to_xts_cm_instrument_list(cm_master_df : pd.DataFrame, series_list_to_include: List[str]= ["EQ","BE","BZ","SM","A","B"])->List[xts_cm_Instrument]:
    """
    Converts the pandas DataFrame of cm_master API to list of xts_cm_Instrument objects.
    Parameters: cm_master_df with pd.DataFrame type & series_list_to_include with list type. Example of List ["EQ","BE","BZ","SM","A","B"].
    Returns: list of XTS Cash Market Instruments.
    """
    xts_cm_Instrument_list = []
    for index, row in cm_master_df.iterrows():
        if(row['Series'] in series_list_to_include):
            xts_cm_Instrument_list.append(xts_cm_Instrument(
            ExchangeSegment = row['ExchangeSegment'],
            ExchangeInstrumentID = row['ExchangeInstrumentID'],
            InstrumentType = row['InstrumentType'],
            Name = row['Name'],
            Description = row['Description'],
            Series = row['Series'],
            NameWithSeries = row['NameWithSeries'],
            InstrumentID = row['InstrumentID'],
            PriceBand_High = row['PriceBand_High'],
            PriceBand_Low = row['PriceBand_Low'],
            FreezeQty = row['FreezeQty'],
            TickSize = row['TickSize'],
            LotSize = row['LotSize'],
            Multiplier = row['Multiplier'],
            DisplayName = row['DisplayName'],
            ISIN = row['ISIN'],
            PriceNumerator = row['PriceNumerator'],
            PriceDenominator = row['PriceDenominator'],
            DetailedDescription = row['DetailedDescription'],
            ExtendedSurvlndicator = row['ExtendedSurvlndicator'],
            Cautionlndicator = row['Cautionlndicator'],
            GSMIndicator = row['GSMIndicator']
            ))
    return xts_cm_Instrument_list

def fo_master_df_to_xts_future_instrument_list(fo_master_df : pd.DataFrame, series_list_to_include: List[str]= ["FUTIDX","FUTSTK","IF"])->List[xts_future_Instrument]:
    """
    Converts the pandas DataFrame of fo_master API to list of xts_future_Instrument objects.
    Parameters: fo_master_df with pd.DataFrame type & series_list_to_include with list type. Example of List ["FUTIDX","FUTSTK","IF"].
    Returns: list of XTS Futures Instruments.
    """
    xts_future_Instrument_list = []
    for index, row in fo_master_df.iterrows():
        if(row['Series'] in series_list_to_include):
            xts_future_Instrument_list.append(xts_future_Instrument(
            ExchangeSegment = row['ExchangeSegment'],
            ExchangeInstrumentID = row['ExchangeInstrumentID'],
            InstrumentType = row['InstrumentType'],
            Name = row['Name'],
            Description = row['Description'],
            Series = row['Series'],
            NameWithSeries = row['NameWithSeries'],
            InstrumentID = row['InstrumentID'],
            PriceBand_High = row['PriceBand_High'],
            PriceBand_Low = row['PriceBand_Low'],
            FreezeQty = row['FreezeQty'],
            TickSize = row['TickSize'],
            LotSize = row['LotSize'],
            Multiplier = row['Multiplier'],
            UnderlyingInstrumentId = row['UnderlyingInstrumentId'],
            UnderlyingIndexName = row['UnderlyingIndexName'],
            ContractExpiration = row['ContractExpiration'],
            DisplayName = row['DisplayName'],
            PriceNumerator = row['PriceNumerator'],
            PriceDenominator = row['PriceDenominator'],
            DetailedDescription = row['DetailedDescription']
            ))
    return xts_future_Instrument_list

def fo_master_df_to_xts_options_instrument_list(fo_master_df : pd.DataFrame, series_list_to_include: List[str]= ["OPTIDX","OPTSTK","IO"])->List[xts_options_Instrument]:
    """
    Converts the pandas DataFrame of fo_master API to list of xts_optoins_Instrument objects
    Parameters: fo_master_df with pd.DataFrame type & series_list_to_include with list type. Example of List : ["OPTIDX","OPTSTK","IO"].
    Returns: list of XTS Options Instruments.
    """
    xts_options_Instrument_list = []
    for index, row in fo_master_df.iterrows():
        if(row['Series'] in series_list_to_include):
            xts_options_Instrument_list.append(xts_options_Instrument(
            ExchangeSegment = row['ExchangeSegment'],
            ExchangeInstrumentID = row['ExchangeInstrumentID'],
            InstrumentType = row['InstrumentType'],
            Name = row['Name'],
            Description = row['Description'],
            Series = row['Series'],
            NameWithSeries = row['NameWithSeries'],
            InstrumentID = row['InstrumentID'],
            PriceBand_High = row['PriceBand_High'],
            PriceBand_Low = row['PriceBand_Low'],
            FreezeQty = row['FreezeQty'],
            TickSize = row['TickSize'],
            LotSize = row['LotSize'],
            Multiplier = row['Multiplier'],
            UnderlyingInstrumentId = row['UnderlyingInstrumentId'],
            UnderlyingIndexName = row['UnderlyingIndexName'],
            ContractExpiration = row['ContractExpiration'],
            StrikePrice = row['StrikePrice'],
            OptionType = row['OptionType'],
            DisplayName = row['DisplayName'],
            PriceNumerator = row['PriceNumerator'],
            PriceDenominator = row['PriceDenominator'],
            DetailedDescription = row['DetailedDescription']
            ))
    return xts_options_Instrument_list

def ohlc_to_df(market_data_get_ohlc_dict: dict):
    """
    Converts XTS-API(from XTS.Connect.get_ohlc()) generated OHLC data to pandas DataFrame.    
    Parameters: The return of XTS.Connect.get_ohlc() method with a type dictionary. Example of dict : {'type': 'success', 'code': 's-instrument-0002', 'description': 'Data found', 'result': {'exchangeSegment': 'NSECM', 'exchangeInstrumentID': '22', 'dataReponse': 'data removed'}}
    Returns: A DataFrame from the OHLC values.
    """
    data_string = market_data_get_ohlc_dict['result']['dataReponse'].replace(',','\n')
    col_headers = ["TimeStamp", "Open", "High", "Low", "Close", "Volume", "OpenInterest"]
    ohlc_df = pd.read_csv(StringIO(data_string), sep = "|",usecols=range(7), low_memory =False)
    ohlc_df.columns = col_headers
    ohlc_df["TimeStamp"] = pd.to_datetime(ohlc_df.TimeStamp, unit="s")
    return ohlc_df

def ticker_exchangeInstrumentId_dict(dataframe_cm:pd.DataFrame):
    """
    IT WORKS ONLY FOR CASH MARKET.
    Converts XTS-API(from XTS.Connect.get_master()-->cm_master_string_to_df/fo_master_string_to_df) DataFrame to a dictionary. So that user can search Instrument Id with ticker symbol.
    Parameters: The return of cm_master_string_to_df/fo_master_string_to_df methods with the type pd.DataFrame.
    Returns: A Dictionary conatining Ticker Symbol as keys & Exchange Instrument Id as values. 
    """
    df = dataframe_cm[['Name','ExchangeInstrumentID']]
    ticker_exchangeInstId_dict = df.set_index('Name')['ExchangeInstrumentID'].to_dict()
    return ticker_exchangeInstId_dict


def dostime_secomds_to_unixtime(_msdostime_inseconds, _timezone = "Asia/Kolkata"):
    """
    This function is used to convert the MS DOS time that is used by NSE & BSE to Unix epoch time.
    * The MS-DOS time/date format uses midnight on January 1, 1980 as a sentinel value, or epoch.
    * Unix epoch starts from  midnight on January 1, 1970.

    The function also allowes to add timezone info to the converted time. by default it will add the timezone info of Asia/Kolkata.
    IMPORTANT: Adding timezone info makes the time aware about time zone. but the value of Uniux will remain UNCHNAGED! 
    """

    _ts_event_dostime_naive = datetime(1980, 1, 1) + timedelta(seconds=int(_msdostime_inseconds)) # naive means this object is unaware about timezone info.
    _timezone = pytz.timezone("Asia/Kolkata")
    _ts_event_dostime_aware = _timezone.localize(_ts_event_dostime_naive) # aware means this object is aware about timezone info.
    #_ts_event_dostime_aware = _ts_event_dostime_naive.replace(tzinfo=timezone(timedelta(hours=_hours, minutes=_minutes))) # aware means this object is aware about timezone info.
    _ts_event_seconds = _ts_event_dostime_aware.astimezone(timezone.utc).timestamp() # in seconds
    _ts_event = _ts_event_seconds  * 1_000_000_000
    return _ts_event

async def async_squareoff_all_positions_(self, exchangeSegment,xt: XTSConnect):
    '''
    It'll squareoff all open positions in the account

    Returns => order_ids : list[]  = contains all squared off orders
    '''

    response_cancelall = await XTSConnect.cancelall_order(self, exchangeSegment=exchangeSegment, exchangeInstrumentID = 0)

    # Retrieve day-wise positions
    response = await XTSConnect.get_position_daywise("*****")

    # Square off any open positions by placing market orders in the opposite direction
    sqrf_order_ids = []
    try:
        for i in response["result"]["positionList"]:
            if int(i["Quantity"]) != 0:
                orde_side = "BUY" if i["Quantity"] < 0 else "SELL"
                sqrf_response = self.xt.place_order(exchangeSegment=i["ExchangeSegment"], exchangeInstrumentID=int(i["ExchangeInstrumentId"]),productType=i["ProductType"],orderType='MARKET',orderSide= orde_side ,timeInForce="DAY",disclosedQuantity= i["Quantity"], orderQuantity= int(i["Quantity"]), limitPrice=0,stopPrice=0,orderUniqueIdentifier='exit_all',clientID="*****")

                sqrf_response
                if sqrf_response.get("result") and sqrf_response["result"].get("AppOrderID"):
                            order_id = response["result"]["AppOrderID"]
                            print(f"Order id : {order_id}")
                            sqrf_order_ids.append(order_id)
                else:
                    print("Failed to place squareoff order:", sqrf_response.get("result", {}).get("AppOrderID"))
        print(f'ssquared off all positions with IDs {sqrf_order_ids}')
        return sqrf_order_ids
    
    except Exception as e:
        print(f"Error exiting order: {e}")
        raise
