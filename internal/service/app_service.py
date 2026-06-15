#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : app_service.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/13 17:36
@Desc    : 应用服务逻辑
"""
import uuid
from dataclasses import dataclass

from injector import inject

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self):
        with self.db.auto_commit():
            # 1.创建模型的实体类
            app = App(name="测试机器人", account_id=uuid.uuid4(), icon="", description="这是一个简单的聊天机器人")
            # 2.将实体类添加到Session会话中
            self.db.session.add(app)
        return app

    def get_app(self, id: uuid.UUID):
        return self.db.session.query(App).get(id)

    def update_app(self, id: uuid.UUID):
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "测试机器人-更新"
        return app

    def delete_app(self, id: uuid.UUID):
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
