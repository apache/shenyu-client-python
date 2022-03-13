# -*- coding: utf-8 -*-

"""
@date:     2021/11/26
@author:   mutian
@version:  1.0
@desc:     module for exception

"""


class GatewayProxyBaseExp(Exception):
    def __init__(self, app_name="", path="", msg="", env=""):
        self.app_name = app_name
        self.path = path
        self.msg = msg
        self.env = env

    def __str__(self):
        return "Gateway Proxy Exception, app_name:{}, path is:({}), msg:{}".format(self.app_name, self.path, self.msg)

    def __repr__(self):
        return self.__str__()


class EnvTypeExp(GatewayProxyBaseExp):
    pass


class SetUpUriExp(GatewayProxyBaseExp):
    pass


class SetUpGatewayExp(GatewayProxyBaseExp):
    pass


class RegisterUriExp(GatewayProxyBaseExp):
    pass


class RegisterMetaDataExp(GatewayProxyBaseExp):
    pass


class RegisterAllMetaDataExp(GatewayProxyBaseExp):
    pass
