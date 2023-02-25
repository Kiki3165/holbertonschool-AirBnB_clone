#!/usr/bin/python3
'''simple def class'''


import json


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
            if hasattr(value, 'to_dict') and callable(getattr(value, 'to_dict')):
                new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    module_name, class_name = class_name.rsplit('.', 1)
                    module = __import__(module_name, globals(), locals(), [class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
