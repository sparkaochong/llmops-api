#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : router.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/11 20:58
@Desc    : 
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    app_handler: AppHandler

    """路由"""

    def register_router(self, app: Flask):
        """注册路由"""

        # 1.创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url与对应的控制器绑定
        # app_handler = AppHandler()
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)
        bp.add_url_rule("/app", methods=["POST"], view_func=self.app_handler.create_app)
        bp.add_url_rule("/app/<uuid:id>", view_func=self.app_handler.get_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["POST"], view_func=self.app_handler.update_app)
        bp.add_url_rule("/app/<uuid:id>/delete", methods=["POST"], view_func=self.app_handler.delete_app)

        # 3.在应用上注册蓝图
        app.register_blueprint(bp)
