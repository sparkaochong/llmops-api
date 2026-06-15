#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : test.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/11 15:56
@Desc    : 
"""
from injector import Injector, inject


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A的Name：{self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
