#!/usr/bin/python3
"""Defines the storage variable"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()