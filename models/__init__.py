#!/usr/bin/python3
"""Initialization of the models directory"""
from models.engine.file_storage import FileStorage

# Create a FileStorage instance for data storage and retrieval
storage = FileStorage()
# Load any previously stored data
storage.reload()

