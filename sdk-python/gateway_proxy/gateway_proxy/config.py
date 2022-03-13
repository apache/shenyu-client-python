# -*- coding: utf-8 -*-

"""
@date:     2021/11/26
@author:   mutian
@version:  1.0
@desc:     module for config

"""
ALL_ENV = ("test", "pre", "prod")


class GatewayConfig:
    """
    If there are multiple gateway registry servers, separated by commas,
    for example: "servers": "10.11.12.12,10.11.12.13"
    """
    # Now only HTTP mode is supported

    register_type = "http"

    test = {
        "servers": "xx.xx.xx.xx",
        "port": 1001
    }
    pre = {
        "servers": "xx.xx.xx.xx",
        "port": 1001
    }
    prod = {
        "servers": "xx.xx.xx.xx",
        "port": 1001
    }

    # Items of configuration that need to be modified according to the project
    uri = {
        "app_name": "app1",                 # app name
        "host": "127.0.0.1",                # python service host
        "port": 8000,                       # python service port
        "context_path": "/xxx",             # context_path
        "environment": "test",              # environment
        "rpc_type": register_type           # rpc type
    }
