from base import BaseCommand
from entity.directory import DirectoryEntity

class MKDir(BaseCommand):
    def __init__(self, directory):
        pass

    def run(self, name):
        new_dir = DirectoryEntity(name, parent=self.directory)
        self.directory.subdirectories.add(new_dir)
