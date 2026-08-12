import os
from dotenv import load_dotenv
load_dotenv()

API_key = os.getenv("XTS_INTERACTIVE_API_KEY")
API_secret = os.getenv("XTS_INTERACTIVE_SECRET_KEY")
API_source = os.getenv("XTS_SOURCE")
API_root = os.getenv("XTS_API_URL")
from xts_api_client.xts_connect_async import XTSConnect
from xts_api_client.helper.helper import cm_master_string_to_df
import asyncio

async def main():
    xt_interactive = XTSConnect(
    apiKey = API_key,
    secretKey = API_secret,
    source = API_source,
    root = API_root
    )
    response_interactive_login = await xt_interactive.interactive_login()
    print(response_interactive_login)
    resp = await xt_interactive.interactive_logout()
    print(resp)
    
if __name__ == "__main__":
    asyncio.run(main())