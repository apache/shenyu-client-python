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

import json

from flask import Flask, jsonify, request

# pip install Apache-ShenYu-Client
from apache_shenyu_client.config import GatewayConfig
from apache_shenyu_client.api import GatewayProxy
from apache_shenyu_client.register import register_uri, register_all_metadata

app = Flask(__name__)

"""  
First, modify the configuration according to the project situation, If you do not configure it, you will not be able to use apache_shenyu_client.   
"""
GatewayConfig.register_type = "http"
GatewayConfig.test = {
    "servers": "172.12.21.10",
    "port": 1001
}
GatewayConfig.pre = {
    "servers": "172.12.21.11",
    "port": 1001
}
GatewayConfig.prod = {
    "servers": "172.12.21.12",
    "port": 1001
}
GatewayConfig.uri = {
    "app_name": "app1",                 # app name
    "host": "172.24.43.8",              # python service host
    "port": 5000,                       # python service port, this service port ois 5000
    "context_path": "/flask_demo",       # context_path
    "environment": "test",              # environment
    "rpc_type": "http"                  # rpc type
}
GatewayConfig.register = {
    "register_type": "http",
    "servers": "172.12.23.10",
    "props": {
        "username": "admin",
        "password": "123456"
    }
}
GatewayConfig.discovery_config = {
    "protocol": "http://",
    "discovery_type": "zookeeper",
    "server_lists": "127.0.0.1:2181",
    "register_path": "/shenyu/discovery/http_example",
    "plugin_name": "",
    "props": {
        "baseSleepTimeMilliseconds": 1000,
        "maxRetries": 4,
        "maxSleepTimeMilliseconds": 5000,
        "connectionTimeoutMilliseconds": 60000,
        "sessionTimeoutMilliseconds": 8
    }
}



"""
Use example
"""

gt = GatewayProxy()
uri = gt.register_uri()
gt.register_metadata(register_all=True)


@register_uri
@register_all_metadata(register_all=True)
def create_app():
    return


@app.route('/userinfo', methods=['POST'])
def hello_world():
    data = request.data.decode("utf-8")
    res = {"code": 200, "msg": "success", "data": "hello world"}
    return jsonify(res)


@app.route('/hel', methods=['GET'])
def hello_world1():
    res = {"code": 200, "msg": "success", "data": "hello world1"}
    return jsonify(res)


@app.route('/hell')
def hello_world2():
    res = {"code": 200, "msg": "success", "data": "hello world2"}
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
