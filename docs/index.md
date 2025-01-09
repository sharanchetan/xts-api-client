# Installation

* This package is written to be used as a XTS API Client in Python.
* With the correct API credentials, User can access XTS interactive & market data.

## Local Server Installation (_recommended_)

* Use __uv packages manager__ to install the package. Example of the command is shown below. (_recommended_)

_Step 1._ 
```
uv add --frozen http://pypi.rmoneyindia.in:8080/xts_api_client-0.1.0-py3-none-any.whl
```
_Step 2._
```
uv sync
```
### Use _PIP_ to install the package. (_not recommended_)
```
pip install http://pypi.rmoneyindia.in:8080/xts_api_client-0.1.0-py3-none-any.whl
```

## Local Installation

* To install the package locally, download the complete zip of the package.
* As per user discretion, use [virtual envirnment](https://docs.python.org/3/library/venv.html) or [uv package manager](https://docs.astral.sh/uv/). Activate the envirnment. ___This is an optional step___ .
* Navigate the __PowerShell/Command prompt__ to the directory (xts_api_client\dist) where __xts_api_client-0.1.0-py3-none-any.whl__ file exists.
* Use "pip install xts_api_client-0.1.0-py3-none-any.whl"
* Use "pip list" or "uv pip list" to verify the installation.

## Pip install/uv add
Currently, the package is not been hosted on the [Python Package Index](https://pypi.org/). So other workarounds are mentioned here to make use of the package.
