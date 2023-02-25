#!/usr/bin/python3
'''class base_model'''


import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    storage = FileStorage()

    def __init__(self, *args, **kwargs):
        '''def'''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        BaseModel.storage.new(self)

    def __str__(self):
        '''def'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''def'''
        self.updated_at = datetime.now()
        BaseModel.storage.save()

    def to_dict(self):
        '''def'''
        dictionary = dict(self.__dict__.copy())
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary