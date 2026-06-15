#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : app_schema.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/12 10:01
@Desc    : 基础聊天接口请求验证
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    # 必填、长度最大为2000
    query = StringField("query", validators=[
        DataRequired(message="用户的提问是必填!"),
        Length(max=2000, message="用户提问最大长度是2000!")
    ])
