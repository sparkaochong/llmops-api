#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : http_code.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/12 10:44
@Desc    : Http基础业务状态码
"""
from enum import Enum


class HttpCode(str, Enum):
    SUCCESS = "success"  # 成功状态
    FAIL = "fail"  # 失败状态
    NOT_FOUND = "not_found"  # 未找到
    UNAUTHORIZED = "unauthorized"  # 未授权
    FORBIDDEN = "forbidden"  # 无权限
    VAILDATE_ERROR = "vaildate_error"  # 数据验证错误
