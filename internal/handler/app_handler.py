#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : app_handler.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/11 20:55
@Desc    : 应用控制器
"""
import os
import uuid
from dataclasses import dataclass

from injector import inject
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, vaildate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id：{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用信息：{app.name}, {app.description}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功更新，新的应用信息：{app.name}, {app.description}")

    def delete_app(self, id: uuid.UUID):
        self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id：{id}")

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入(Post)
        req = CompletionReq()
        if not req.validate():
            return vaildate_error_json(req.errors)
        # 2.构建组件
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="gpt-4o-mini", base_url=os.getenv("OPENAI_BASE_URL"))
        parser = StrOutputParser()

        # 3.构建链
        chain = prompt | llm | parser

        # 4.调用链
        content = chain.invoke({"query": req.query.data})

        return success_json({"content": content})

    """测试"""

    def ping(self):
        # return {"ping": "pong"}
        raise FailException("数据未找到")
