#!/usr/bin/python3

import uuid
from datetime import datetime
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    def __init__(self, *args, **kwargs):
        """you will use *args, **kwargs arguments for
           the constructor of a BaseModel
        """
        if kwargs:
            self.__dict__ = kwargs
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], time)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """print the class name, id and directory"""

        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values in dic"""

        new_dict = self.__dict__.copy()
        if 'created_at' in new_dict:
            new_dict.update(
                {'created_at': new_dict['created_at'].strftime(time)})
        if 'updated_at' in new_dict:
            new_dict.update(
                {'updated_at': new_dict['updated_at'].strftime(time)})
        new_dict.update({'__class__': self.__class__.__name__})
        return new_dict
