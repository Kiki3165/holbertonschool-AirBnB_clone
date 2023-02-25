#!/usr/bin/python3
'''simple def class'''


import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''def'''
        return self.__objects

    def new(self, obj):
        '''def'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''def'''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        '''def'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects_dict = json.load(f)
                for k, v in objects_dict.items():
                    class_name, obj_id = k.split('.')
                    class_obj = eval(class_name)
                    self.new(class_obj(**v))
        except FileNotFoundError:
            pass
