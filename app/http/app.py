#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : app.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/11 21:20
@Desc    : 
"""
import dotenv
from flask_migrate import Migrate
from injector import Injector

from app.http.module import ExtensionMoudle
from config import Config
from internal.router import Router
from internal.server import Http
from pkg.sqlalchemy import SQLAlchemy

# 将env加载到环境变量中
dotenv.load_dotenv()

injector = Injector([ExtensionMoudle])

conf = Config()

app = Http(
    __name__,
    conf=conf,
    db=injector.get(SQLAlchemy),
    migrate=injector.get(Migrate),
    router=injector.get(Router)
)

if __name__ == "__main__":
    app.run(debug=True)
