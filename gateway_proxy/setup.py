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

from setuptools import setup

setup(
    name="gateway_proxy",                                               # project name, pip3 install gateway_proxy
    version="0.1.0",                                                    # version
    author="mutianzhang",                                               # author
    author_email="mutianzero@gmail.com",                                # email
    url="https://github.com/mutianzero/incubator-shenyu-client-python", # project repo url
    description="shenyu python proxy service sdk",                      # description
    packages=["gateway_proxy"],                                         # packages name
    install_requires=["requests>=2.25.1", "PyYAML>=5.3"],               # requires third packages
    python_requires=">=3.6",                                            # python version condition
    entry_points={                                                      # console scripts
        "console_scripts": [
            "gp-help=gateway_proxy:get_help",
            "gp-doc=gateway_proxy:get_doc"
        ]
    }
)
