from  decimal import Decimal

class xts_future_Instrument():
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
                ContractExpiration: str,
                DisplayName: str,
                PriceNumerator: int,
                PriceDenominator: int,
                DetailedDescription: str
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
        self.ContractExpiration = ContractExpiration
        self.DisplayName = DisplayName
        self.PriceNumerator = PriceNumerator
        self.PriceDenominator = PriceDenominator
        self.DetailedDescription = DetailedDescription
    
    def __repr__(self):
        return(f"xts_future_instrument_Name={self.Name},
               ExchangeInstrumentID={self.ExchangeInstrumentID},
               Series= {self.Series},
               InstrumentID={self.InstrumentID},
               ExchangeSegment={self.ExchangeSegment},
               LotSize={self.LotSize}"
               )
        