#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import inspect
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            d = [
                    k
                    for k, v in inspect.getmembers(
                        sys.modules[__name__],
                        inspect.isclass
                        )
                    ]
            if cls in d or cls.__name__ in d:
                return {
                        key: value
                        for key, value in self.__objects.items()
                        if value.__class__.__name__ is cls or
                        value.__class__ is cls
                        }
            else:
                return dict()
        return self.__objects
    
    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj


    def news(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object"""
        if obj:
            try:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                self.__objects.pop(key)
            # shouldnt do anyhting
            except Exception:
                pass

    def close(self):
        """ calls reload"""
        self.reload()
