#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : test_app_handler.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/12 15:50
@Desc    : APP控制器的测试类
"""
from pprint import pprint

import pytest

from pkg.response import HttpCode


@pytest.mark.parametrize("query", [None, "你好，你是谁？"], ids=["空查询-应返回验证错误", "正常查询-应返回成功"])
class TestAppHandler:
    def test_completion(self, query, client):
        resp = client.post("/app/completion", json={"query": query})
        assert resp.status_code == 200
        if query is None:
            assert resp.json.get("code") == HttpCode.VAILDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
        print("响应内容:")
        pprint(resp.json)
