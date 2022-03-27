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

from copy import deepcopy
from functools import wraps

from gateway_proxy.gateway_proxy.api import GatewayProxy
from gateway_proxy.gateway_proxy.exception import (RegisterUriExp, RegisterMetaDataExp, RegisterAllMetaDataExp)


def register_uri(func):
    @wraps(func)
    def _register_uri():
        try:
            gt = GatewayProxy()
            gt.register_uri()
            func()
        except RegisterUriExp as e:
            raise RegisterUriExp()
        except Exception as e:
            print("register_uri except, detail is:{}".format(str(e)))
            raise e
    return _register_uri


def register_metadata(**kwargs):
    def register_decorator(func):
        @wraps(func)
        def _wrapped_register_metadata():
            try:
                gt = GatewayProxy()
                gt.register_metadata(**kwargs)
                func()
            except RegisterMetaDataExp as ee:
                raise ee
            except Exception as e:
                print("register_metadata except, detail is:{}".format(str(e)))
                raise e
        return _wrapped_register_metadata
    return register_decorator


def register_all_metadata(**kwargs):
    def register_all_metadata_decorator(func):
        @wraps(func)
        def _wrapped_register_all_metadata():
            try:
                gt = GatewayProxy()
                _kwargs = deepcopy(kwargs)
                _kwargs.update({"register_all": True})
                gt.register_metadata(**_kwargs)
                func()
            except RegisterAllMetaDataExp as ee:
                raise ee
            except Exception as e:
                print("register_all_metadata except, detail is:{}".format(str(e)))
                raise e
        return _wrapped_register_all_metadata
    return register_all_metadata_decorator
