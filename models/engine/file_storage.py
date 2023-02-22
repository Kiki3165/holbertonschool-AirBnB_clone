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

    def reload(self):
        '''simple def'''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    module_name = 'models.' + class_name.lower()
                    cls = getattr(__import__(module_name, fromlist=[class_name]), class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
