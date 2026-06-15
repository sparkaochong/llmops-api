#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project : llmops-api
@File    : app.py
@Author  : aochong
@Email   : sparkaochong@gmail.com
@Date    : 2026/6/13 17:16
@Desc    : AI应用基础模型类
"""
import uuid
from datetime import datetime

from sqlalchemy import (
    Column,
    UUID,
    String,
    Text,
    DateTime,
    PrimaryKeyConstraint,
    Index
)

from internal.extension.database_extension import db


class App(db.Model):
    __table_name__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_app_id"),
        Index("idx_app_account_id", "account_id")
    )

    id = Column(UUID, default=uuid.uuid4(), nullable=False)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    status = Column(String(255), default="", nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
