# -*- coding: utf-8 -*-
"""
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
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

    register = {
        "register_type": "http",
        "servers": "xx.xx.xx.xx",
        "namespace_id": "testNamespaceId",
        "props": {
            "username": "admin",
            "password": "123456"
        }
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

    discovery_config = {
        "protocol": "http://",                             # protocol
        "discovery_type": "zookeeper",                     # discovery type
        "server_lists": "127.0.0.1:2181",                  # server lists
        "register_path": "/shenyu/discovery/http_example", # register path
        "plugin_name": "",                                 # plugin name
        "props": {
            "baseSleepTimeMilliseconds": 1000,             # base sleep time milliseconds
            "maxRetries": 4,                               # max retries
            "maxSleepTimeMilliseconds": 5000,              # max sleep time milliseconds
            "connectionTimeoutMilliseconds": 60000,        # connection timeout milliseconds
            "sessionTimeoutMilliseconds": 8                # session timeout milliseconds
        }
        # "discovery_type": "nacos",
        # "server_lists": "http://127.0.0.1:8848",
        # "register_path": "/shenyu/discovery/http_example",
        # "discovery_type": "eureka",
        # "server_lists": "http://127.0.0.1:8761/eureka",
        # "register_path": "shenyu_discovery_http_example",
        # "discovery_type": "etcd",
        # "server_lists": "http://127.0.0.1:2379",
        # "register_path": "shenyu_discovery_http_example",
    }
