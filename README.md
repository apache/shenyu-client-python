## Apache-ShenYu-Client  
Apache-Shenyu-Client for python client allows you to access ShenYu Gateway, it supports registory python service to ShenYu Gateway.

### Requirements   
Supported python version over 3.6
Supported ShenYu version over 2.4.3

### instructions
> 1、install  
pip3 install Apache-ShenYu-Client -i https://pypi.python.org/simple

> 2、usage

> 3.1、Use the decorator
```
>>import package:      

from apache_shenyu_client.config import GatewayConfig
from apache_shenyu_client.register import register_uri, register_metadata, register_all_metadata

3.1.0、First, modify the configuration according to the project situation, If you do not configure it, you will not be able to use apache_shenyu_client.   
#### Configure shenyu gateway services and port 
GatewayConfig.test = {
        "servers": "xx.xx.xx.xx",
        "port": 1001
    }   
#### Configure python services information   
GatewayConfig.uri = {
        "app_name": "app2",             # app name
        "host": "172.24.43.28",         # python service host
        "port": 8000,                   # python service port
        "context_path": "/flask_test",   # context_path
        "environment": "test",          # environment
        "rpc_type": "http"              # rpc type
    }       
#### Configure to get administrator token
GatewayConfig.register = {
        "register_type": "http",
        "servers": "xx.xx.xx.xx",
        "props": {
            "username": "admin",
            "password": "123456"
        }
    }

3.1.1、proxy all api

3.1.1.1、Using a decorator at the entry of a service request to register for this service: @register_uri 
3.1.1.2、Using a decorator at the entry of a service request: @register_all_metadata(register_all=True)

3.1.2、proxy some api
3.1.2.1、Using a decorator at the entry of a service request to register for this service: @register_uri 
3.1.2.2、use a decorator on that api definition: @register_metadata，need param: path, as follows 3.1.2.3:

3.1.2.3、this is a python flask service api, path is "/search"
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

from apache_shenyu_client.config import GatewayConfig
from apache_shenyu_client.api import GatewayProxy
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
