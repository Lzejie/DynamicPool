# -*- coding: utf-8 -*-
# @Time    : 18/12/10 上午10:27
# @Author  : L_zejie
# @Site    :
# @File    : setup.py.py
# @Software: PyCharm Community Edition

from setuptools import setup, find_packages

setup(
    name="DynamicPool",
    packages=find_packages(),
    version='0.14',
    description="动态任务阻塞线程/进程池",
    author="L_zejie",
    author_email='lzj_xuexi@163.com',
    url="https://github.com/Lzejie/DynamicPool",
    license="MIT Licence",
    keywords=["Thread Pool", "Dynamic Pool", "Dynamic Thread Pool", "Dynamic Process Pool"],
    classifiers=[],
    install_requires=[]
)
