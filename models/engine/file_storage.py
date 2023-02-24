#!/usr/bin/python3
'''simple def class'''


import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    module_name = value['__class__']
                    class_name = module_name.split(".")[1]
                    module = __import__('models.' + module_name, fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj = class_(**value)
                    FileStorage.__objects[key] = obj
        except:
            pass
