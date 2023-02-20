#!/usr/bin/python3
'''class base_model'''

import uuid
import datetime
import json

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
    x = str(id)
    print(type(x))

    created_at = datetime.datetime.now()
    print(type(created_at))
    updated_at = datetime.datetime.now()
    
    @staticmethod
    def save(dictionnaries):
        '''def save'''
        if dictionnaries is None or len(dictionnaries) == 0:
            return "[]"
        else:
            return json.dumps(dictionnaries)
