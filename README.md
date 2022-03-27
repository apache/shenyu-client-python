## proxy python service gateway request

### detail doc

[How to access the gateway for http services in non-java languages](https://github.com/apache/incubator-shenyu-sdk/sdk-python/)

### instructions
> 1、install  
pip3 install gateway-proxy

> 2、usage

> 3.1、Use the decorator
```
>>import package:
from gateway_proxy.config import GatewayConfig
from gateway_proxy.register import register_uri, register_metadata, register_all_metadata

3.1.0、Modify the configuration according to the project situation

GatewayConfig.uri = {
        "app_name": "app2",             # app name
        "host": "172.24.43.28",         # python service host
        "port": 8000,                   # python service port
        "context_path": "/flask_test",   # context_path
        "environment": "test",          # environment
        "rpc_type": "http"              # rpc type
    }

3.1.1、proxy all interfaces

3.1.1.1、Using a decorator at the entry of a service request to register for this service: @register_uri 
3.1.1.2、Using a decorator at the entry of a service request: @register_all_metadata(register_all=True)

3.1.2、proxy some interface
3.1.2.1、Using a decorator at the entry of a service request to register for this service: @register_uri 
3.1.2.2、use a decorator on that interface definition: @register_metadata，need param: path, as follows 3.1.2.3:

3.1.2.3、this is a python flask service interface, path is "/search"
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

> 3.2、function call usage
```
>>import package

from gateway_proxy.config import GatewayConfig
from gateway_proxy.api import GatewayProxy
gt = GatewayProxy()

3.2.1、Modify the configuration according to the project situation
GatewayConfig.uri = {
        "app_name": "app2",            # app name
        "host": "172.24.43.28",        # python service host
        "port": 8000,                  # python service port
        "context_path": "/flask_test",  # context_path
        "environment": "test",         # environment
        "rpc_type": "http"             # rpc type
    }

3.2.2、register uri: gt.register_uri()

"/helloqq2" is the path to register  

3.2.2.1、register some path:   
gt.register_metadata("/helloqq2")

3.2.2.1、register all path:   
gt.register_metadata(register_all=True)
```
