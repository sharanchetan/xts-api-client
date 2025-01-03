import pandas as pd
from xts_api_client.helper.xts_cm_instrument import xts_cm_Instrument
from xts_api_client.helper.xts_cm_instrument import xts_cm_Instrument
from xts_api_client.helper.xts_future_instrument import xts_future_Instrument
from xts_api_client.helper.xts_options_instrument import xts_options_Instrument
from typing import List
from io import StringIO
from decimal import Decimal



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
    Converts XTS-API(from XTS.Connect.get_master()-->cm_master_string_to_df/fo_master_string_to_df) DataFrame to a dictionary. So that user can search Instrument Id with ticker symbol.
    Parameters: The return of cm_master_string_to_df/fo_master_string_to_df methods with the type pd.DataFrame.
    Returns: A Dictionary conatining Ticker Symbol as keys & Exchange Instrument Id as values. 
    """
    df = dataframe_cm[['Name','ExchangeInstrumentID']]
    ticker_exchangeInstId_dict = df.set_index('Name')['ExchangeInstrumentID'].to_dict()
    return ticker_exchangeInstId_dict