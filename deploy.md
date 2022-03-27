# How to deploy?

### 1、Register a repository account
1.1、First, you need to register an account on the PyPI website or your own central repository account.   
1.2、Pypi register url is: https://pypi.org/account/register/   

### 2、Upload package
2.1、You can upload package to Pypi or your own central repository, if you choose pypi, you can do as next. 
2.2、Change to the project root directory and execute the commands in turn，
2.2.1、python setup.py register
2.2.2、python setup.py sdist upload

### 3、Use
3.1、If you successfully upload package to pypi, you can install using pip, such as: pip install gateway-proxy