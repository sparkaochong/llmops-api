#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : default_config.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/12 18:30
@Desc    : 应用默认配置项
"""
DEFAULT_CONFIG = {
    # 开发暂时关闭WTF的CSRF保护(生产需要开启)
    "WTF_CSRF_ENABLED": "False",
    # SQLALCHEMY数据库配置
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_POOL_SIZE": 30,
    "SQLALCHEMY_POOL_RECYCLE": 3600,
    "SQLALCHEMY_ECHO": "True"
}
