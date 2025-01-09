# Package Structure
* To better consume the package, the user should have a clear understanding of the architecture of the package.

Here is the folder structure of the project:

```
└───xts_api_client
    │   interactive_socket.py
    │   interactive_socket_client.py
    │   market_data_socket.py
    │   market_data_socket_client.py
    │   py.typed
    │   xts_connect.py
    │   xts_connect_async.py
    │   xts_exception.py
    │   __init__.py
    │   
    ├───helper
        helper.py
        helper_classes.py
        __init__.py
```

There are two version of xts_connect. A synchronous version & an Asynchronous version.

## xts_connect.py
* This module is written for simple test cases & basic understanding of the API, however in practical cases, user will have to use Asynchronous methods.
## xts_connect_async.py
* For all intensive purposes, this module will be used only because of the nature of application.