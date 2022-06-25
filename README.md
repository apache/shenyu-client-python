## Apache-ShenYu-Client

[![Build and Test](https://github.com/apache/incubator-shenyu-client-python/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/apache/incubator-shenyu-client-python/actions)
[![codecov.io](https://codecov.io/gh/apache/incubator-shenyu-client-python/coverage.svg?branch=main)](https://app.codecov.io/gh/apache/incubator-shenyu-client-python?branch=main)

Apache-Shenyu-Client for python client allows you to access ShenYu Gateway, it supports registry python service to ShenYu Gateway.

### Requirements

- python3.6+
- ShenYu2.4.3+

### Install

`pip3 install Apache-ShenYu-Client -i https://pypi.python.org/simple`

### Usage

#### Use the decorator
```
import package:      

from apache_shenyu_client.config import GatewayConfig
from apache_shenyu_client.register import register_uri, register_metadata, register_all_metadata
```
_First, modify the configuration according to the project situation, If you do not configure it, you will not be able to use apache_shenyu_client._

- Configure shenyu gateway services and port 
```
GatewayConfig.test = {
        "servers": "xx.xx.xx.xx",
        "port": 1001
    }
```
- Configure python services information
```
GatewayConfig.uri = {
        "app_name": "app2",             # app name
        "host": "172.24.43.28",         # python service host
        "port": 8000,                   # python service port
        "context_path": "/flask_test",   # context_path
        "environment": "test",          # environment
        "rpc_type": "http"              # rpc type
    }
```
- Configure to get administrator token
```
GatewayConfig.register = {
        "register_type": "http",
        "servers": "xx.xx.xx.xx",
        "props": {
            "username": "admin",
            "password": "123456"
        }
    }
```
- Proxy all api
  - Using a decorator at the entry of a service request to register for this service: `@register_uri`
  - Using a decorator at the entry of a service request: `@register_all_metadata(register_all=True)`

- Proxy some api
  - Using a decorator at the entry of a service request to register for this service: @register_uri 
  - Use a decorator on that api definition: @register_metadata，need param: path, as follows 3.1.2.3:
  - This is a python flask service api, path is "/search"
    ```
    @user.route('/search', methods=['GET'])
    def user_search_handler():
        data = UserBusiness.search_by_nickname()
        return json_detail_render(0, data)`
    
    proxy：
    @register_metadata("/search")
    @user.route('/search', methods=['GET'])
    def user_search_handler():
        data = UserBusiness.search_by_nickname()
        return json_detail_render(0, data)
    
    ```

#### Function call usage

```
import package

from apache_shenyu_client.config import GatewayConfig
from apache_shenyu_client.api import GatewayProxy
gt = GatewayProxy()
```
- Modify the configuration according to the project situation
```
GatewayConfig.uri = {
        "app_name": "app2",            # app name
        "host": "172.24.43.28",        # python service host
        "port": 8000,                  # python service port
        "context_path": "/flask_test",  # context_path
        "environment": "test",         # environment
        "rpc_type": "http"             # rpc type
    }
```
- Register uri

    ```gt.register_uri()``` and `"/helloqq2"` is the path to register  

  - register some path:
    ```
    gt.register_metadata("/helloqq2")
    ```
  - register all path:
    ```
    gt.register_metadata(register_all=True)
    ```
