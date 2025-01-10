# How To Guide for Package

## Native Functions/Methods available in package.
* Most of these functions are self explanatory in nature. However, a simple explanations is mentioned for them.
*  The __Trading API__ gives the user access to 
      *  __interactive_login__: Send the login url to which a user should receive the token.
      *  __get_order_book__: Request order book gives states of all the orders placed by an user.
      *  __get_dealer_orderbook__: No idea, figure it out yourself!
      *  __place_order__: To place an order.
      *  __place_bracketorder__: To place a bracketorder.
      *  __get_profile__: Using session token user can access his profile stored with the broker.
      *  __get_balance__: Get balance API call grouped under this category information related to limits on equities, derivative, upfront margin, available exposure and other RMS related balances available to the user.
      *  __modify_order__: The facility to modify your open orders by allowing you to change limit order to market or vice versa, change price or quantity of the limit open order, change disclosed quantity or stop-loss of any open stop loss order.
      *  __get_trade__: Trade book returns a list of all trades executed on a particular day, that were placed by the user. The trade book will display all filled and partially filled orders.
      *  __get_dealer_tradebook__: Trade book returns a list of all trades executed on a particular day, that were placed by the user. The trade book will display all filled and partially filled orders.
      *  __get_holding__: Holdings API call enable users to check their long term holdings with the broker.
      *  __bracketorder_cancel__: This API can be called to cancel any open order of the user by providing correct appOrderID matching with the chosen open order to cancel.
      *  __get_dealerposition_netwise__: The positions API positions by net. Net is the actual, current net position portfolio.
      *  __get_dealerposition_daywise__: The positions API returns positions by day, which is a snapshot of the buying and selling activity for that particular day.
      *  __get_position_daywise__: The positions API returns positions by day, which is a snapshot of the buying and selling activity for that particular day.
      *  __get_position_netwise__: The positions API positions by net. Net is the actual, current net position portfolio.
      *  __convert_position__: Convert position API, enable users to convert their open positions from NRML intra-day to Short term MIS or vice versa, provided that there is sufficient margin or funds in the account to effect such conversion.
      *  __cancel_order__: This API can be called to cancel any open order of the user by providing correct appOrderID matching with the chosen open order to cancel.
      *  __cancelall_order__: This API can be called to cancel all open order of the user by providing exchange segment and exchange instrument ID.
      *  __place_cover_order__: A Cover Order is an advance intraday order that is accompanied by a compulsory Stop Loss Order. This helps users to minimize their losses by safeguarding themselves from unexpected market movements. A Cover Order offers high leverage and is available in Equity Cash, Equity F&O, Commodity F&O and Currency F&O segments. It has 2 orders embedded in itself, they are Limit/Market Order Stop Loss Order.
      *  __exit_cover_order__: Exit Cover API is a functionality to enable user to easily exit an open stoploss order by converting it into Exit order.
      *  __squareoff_position__: User can request square off to close all his positions in Equities, Futures and Option. Users are advised to use this request with caution if one has short term holdings.
      *  __get_order_history__: Order history will provide particular order trail chain. This indicate the particular order & its state changes. i.e.Pending New to New, New to PartiallyFilled, PartiallyFilled, PartiallyFilled & PartiallyFilled to Filled etc.
      *  __interactive_logout__: This call invalidates the session token and destroys the API session. After this, the user should go through login flow again and extract session token from login response before further activities.

*  The __Market Data API__ gives the user access to 
      *  __marketdata_login__: Send the login url to which a user should receive the token.
      *  __get_config__: Get the configuration of the client.
      *  __get_quote__: Get the quote of the instrument.
      *  __send_subscription__: Send subscription for the instrument.
      *  __send_unsubscription__: Send un subscription for the instrument.
      *  __get_master__: Get the master string.
      *  __get_ohlc__: Get the OHLC of the instrument.
      *  __get_series__: Get the series of the exchange segment.
      *  __get_equity_symbol__: Get the equity symbol of the exchange segment.
      *  __get_expiry_date__: Get the expiry date of the exchange segment.
      *  __get_future_symbol__: Get the future symbol of the exchange segment.
      *  __get_option_symbol__: Get the option symbol of the exchange segment.
      *  __get_option_type__: Get the option type of the exchange segment.
      *  __get_index_list__: Get the index list of the exchange segment.
      *  __search_by_instrumentid__: Search by instrument id.
      *  __search_by_scriptname__: Search by script name.
      *  __marketdata_logout__: This call invalidates the session token and destroys the API session.
