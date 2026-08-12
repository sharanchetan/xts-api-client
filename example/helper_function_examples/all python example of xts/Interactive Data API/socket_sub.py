import os
from dotenv import load_dotenv
load_dotenv()
from xts_api_client.xts_connect_async import XTSConnect
import asyncio

API_key = os.getenv("XTS_Interactive_API_KEY")
API_secret = os.getenv("XTS_Interactive_SECRET_KEY")
API_source = os.getenv("XTS_SOURCE")
API_root = os.getenv("XTS_API_URL")

async def main():
    xt_interactive_data = XTSConnect(
    apiKey = API_key,
    secretKey = API_secret,
    source = API_source,
    root = API_root
    )

    response_interactive_login = await xt_interactive_data.interactive_login()
    response_subs = await xt_interactive_data.send_subscription(Instruments=[{'exchangeSegment':1,'exchangeInstrumentID':26000}], xtsMessageCode=1501)
    print(response_subs['result'])

if __name__ == "__main__":
    asyncio.run(main())   