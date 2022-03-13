# -*- coding: utf-8 -*-

"""
@date:     2021/11/26
@author:   mutian
@version:  1.0
@desc:     common module

"""
from copy import deepcopy
from functools import wraps

from gateway_proxy.api import GatewayProxy
from gateway_proxy.exception import (RegisterUriExp,
                                     RegisterMetaDataExp,
                                     RegisterAllMetaDataExp)


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
