# -*- coding: utf-8 -*-

"""
@date:     2021/11/27
@author:   mutian
@version:  1.0
@desc:     module for setup

"""
from setuptools import setup

setup(
    name="gateway_proxy",                                            # project name, pip3 install gateway_proxy
    version="0.1.0",                                                 # version
    author="mutianzhang",                                            # author
    author_email="mutianzero@gmail.com",                             # email
    url="https://github.com/apache/incubator-shenyu-sdk/sdk-python", # project repo url
    description="shenyu python proxy service sdk",                   # description
    packages=["gateway_proxy"],                                      # packages name
    install_requires=["requests>=2.25.1", "PyYAML>=5.3"],            # requires third packages
    python_requires=">=3.6",                                         # python version condition
    entry_points={                                                   # console scripts
        "console_scripts": [
            "gp-help=gateway_proxy:get_help",
            "gp-doc=gateway_proxy:get_doc"
        ]
    }
)
