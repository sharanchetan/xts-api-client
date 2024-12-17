import pandas as pd
from xts_api_client.helper.xts_cm_instrument import xts_cm_Instrument
from xts_api_client.helper.xts_cm_instrument import xts_cm_Instrument
from xts_api_client.helper.xts_future_instrument import xts_future_Instrument
from xts_api_client.helper.xts_options_instrument import xts_options_Instrument
from typing import List
from io import StringIO

def cm_master_string_to_df(cm_master_result :str)->pd.DataFrame:
    """
        Convert the response of cm_master API to a pandas DataFrame.
        This function takes a string response from the cm_master API, which contains
        data separated by the '|' character, and converts it into a pandas DataFrame.
        The DataFrame will have predefined column headers.
        Parameters:
        cm_master_result (str): The string response from the cm_master API.
        Returns:
        pd.DataFrame: A pandas DataFrame containing the parsed data from the cm_master_result string.
    """
    col_header = "ExchangeSegment|ExchangelnstrumentlD|InstrumentType|Name|Description|Series|NameWithSeries|InstrumentlD|PriceBand.High|PriceBand.Low|FreezeQty|TickSize|LotSize|Multiplier|DisplayName|ISIN|PriceNumerator|PriceDenominator|DetailedDescription|ExtendedSurvlndicator|Cautionlndicator|GSMIndicator".split("|")   
    cm_master_df = pd.read_csv(StringIO(cm_master_result), sep = "|", usecols=range(22), low_memory =False)
    cm_master_df.columns = col_header
    return cm_master_df

def fo_master_string_to_df(fo_master_result :str)->pd.DataFrame:
    """
        Convert the response of master API to pandas DataFrame for fo segment.
        This function takes a string response from the fo_master API, splits it into lines,
        and then categorizes each line into futures or options based on the number of columns.
        It then converts these categorized lines into pandas DataFrames with appropriate column headers.
        Parameters:
        fo_master_result (str): The string response from the fo_master API.
        Returns:
        tuple: A tuple containing two pandas DataFrames:
            - fut_master_df: DataFrame containing futures data.
            - opt_master_df: DataFrame containing options data.
    """
    opt_col_header = "ExchangeSegment|ExchangelnstrumentlD|InstrumentType|Name|Description|Series|NameWithSeries|InstrumentID|PriceBand.High|PriceBand.Low|FreezeQty|TickSize|LotSize|Multiplier|UnderlyinglnstrumentId|UnderlyinglndexName|ContractExpiration|StrikePrice|OptionType|DisplayName|PriceNumerator|PriceDenominator|DetailedDescription".split("|")
    fut_col_header = "ExchangeSegment|ExchangelnstrumentlD|InstrumentType|Name|Description|Series|NameWithSeries|InstrumentID|PriceBand.High|PriceBand.Low|FreezeQty|TickSize|LotSize|Multiplier|UnderlyinglnstrumentId|UnderlyinglndexName|ContractExpiration|DisplayName|PriceNumerator|PriceDenominator|DetailedDescription".split("|")
    fut_lines = []
    opt_lines = []
    lines = fo_master_result.split("\n")
    for a in lines:
        b= a.split("|")
        if len(b) == 23:
            pass
            opt_lines.append(a)            
        else:
            pass
            fut_lines.append(a)
     
    fut_string = "\n".join(fut_lines)
    opt_string = "\n".join(opt_lines)

    fut_master_df = pd.read_csv(StringIO(fut_string), sep = "|", low_memory =False)
    fut_master_df.columns = fut_col_header

    opt_master_df = pd.read_csv(StringIO(opt_string), sep = "|", low_memory =False)
    opt_master_df.columns = opt_col_header
    return fut_master_df, opt_master_df

def cm_master_df_to_xts_cm_instrument_list(cm_master_df : pd.DataFrame, series_list_to_include: List[str]= ["EQ","BE","BZ","SM","A","B"])->List[xts_cm_Instrument]:
    """
    Convert the pandas DataFrame of cm_master API to list of xts_cm_Instrument objects
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
    Convert the pandas DataFrame of fo_master API to list of xts_future_Instrument objects
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