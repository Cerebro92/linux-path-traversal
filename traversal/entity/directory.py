from datetime import datetime
from entity.base import BaseEntity


class DirectoryEntity(BaseEntity):
    def __init__(self, name, parent=None, subdirectories=None):
        super(DirectoryEntity, self).__init__(name)
        if not subdirectories:
            subdirectories = []
        self.subdirectories = subdirectories
        self.parent = parent
        self.created_at = datetime.now()

    def add(self, _dir):
        self.subdirectories.append(_dir)
        return self.subdirectories

    def remove(self, _dir):
        self.subdirectories.remove(_dir)
        return self.subdirectories

    def find_subdirectory_by_name(self, name):
        # time complexity - O(# of subdirectories)
        # optimize this!
        # Use a dict
        for _dir in self.subdirectories:
            if _dir.name == name:
                return _dir

    def serialize(self):
        details = {
            'name': self.name,
            'created_at': self.created_at
        }
        return details

