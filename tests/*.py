import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage




class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.storage.new(self.base_model)
        self.storage.save()

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)
        self.assertIn("BaseModel.{}".format(self.base_model.id), all_objects)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_model.id), all_objects)

    def test_save(self):
        with open("file.json", "r") as f:
            file_contents = f.read()
            self.assertIn("BaseModel.{}".format(self.base_model.id), file_contents)

    def test_reload(self):
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.base_model.id), all_objects)

    def test_deserialize_base_model(self):
        with open("file.json", "r") as f:
            file_contents = f.read()
        obj_dict = eval(file_contents)
        new_model = BaseModel(**obj_dict["BaseModel.{}".format(self.base_model.id)])
        self.assertEqual(type(new_model), BaseModel)
        self.assertEqual(new_model.id, self.base_model.id)
