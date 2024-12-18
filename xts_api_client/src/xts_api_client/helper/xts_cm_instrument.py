from  decimal import Decimal

class xts_cm_Instrument():
    def __init__(self,
                ExchangeSegment: str,
                ExchangeInstrumentID: int,
                InstrumentType: int,
                Name: str,
                Description: str,
                Series: str,
                NameWithSeries: str,
                InstrumentID: int,
                PriceBand_High: Decimal,
                PriceBand_Low: Decimal,
                FreezeQty: int,
                TickSize: Decimal,
                LotSize: int,
                Multiplier: Decimal,
                DisplayName: str,
                ISIN: str,
                PriceNumerator: int,
                PriceDenominator: int,
                DetailedDescription: str,
                ExtendedSurvlndicator: int,
                Cautionlndicator: int,
                GSMIndicator: int
                ):
        self.ExchangeSegment = ExchangeSegment
        self.ExchangeInstrumentID = ExchangeInstrumentID
        self.InstrumentType = InstrumentType
        self.Name = Name   
        self.Description = Description
        self.Series = Series
        self.NameWithSeries = NameWithSeries
        self.InstrumentID = InstrumentID
        self.PriceBand_High = PriceBand_High
        self.PriceBand_Low = PriceBand_Low
        self.FreezeQty = FreezeQty
        self.TickSize = TickSize
        self.LotSize = LotSize
        self.Multiplier = Multiplier
        self.DisplayName = DisplayName
        self.ISIN = ISIN
        self.PriceNumerator = PriceNumerator
        self.PriceDenominator = PriceDenominator
        self.DetailedDescription = DetailedDescription
        self.ExtendedSurvlndicator = ExtendedSurvlndicator
        self.Cautionlndicator = Cautionlndicator
        self.GSMIndicator = GSMIndicator
        
    def __repr__(self):
        return (f"xts_cm_Instrument_Name={self.Name}, Series={self.Series}, ExchangeSegment={self.ExchangeSegment}, InstrumentID={self.InstrumentID}")