#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : module.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/12 18:47
@Desc    : 
"""
from flask_migrate import Migrate
from injector import Module

from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy


class ExtensionMoudle(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
