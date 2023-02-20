#!/usr/bin/python3
'''class base_model'''

import uuid
import datetime

'''def class'''

class BaseModel:
    __nb_object = 0
    
    def __init__(self, id):
        '''constructor'''

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_object += 1
            self.id = self.__class__.__nb_object

    id = uuid.uuid4()
    s = str(id)
    print('Type', type(id), 'UUID', id)

    created_at = datetime.datetime.now()
    print(created_at)

    updated_at = datetime.datetime.now()
    print(updated_at)

    def __str__(self):
        '''def str'''
        
        return f"[BaseModel] [{self.id}] [{self.__dict__}]"

    def save(self):
        '''def save'''
        
        return self.updated_at.replace(year=2000)

    def to_dict(self):
        '''def to_dict'''
        
        return f"[{self.id}] [{self.__dict__}]"
