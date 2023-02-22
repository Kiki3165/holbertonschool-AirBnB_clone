#!/usr/bin/python3
'''simple def class'''


import json
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''simple def'''
        return FileStorage.__objects

    def new(self, obj):
        '''simple def'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''simple def'''
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f, indent=4)
