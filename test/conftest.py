#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : conftest.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/12 16:36
@Desc    : 获取FLask应用的测试应用并返回
"""
import pytest

from app.http.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
