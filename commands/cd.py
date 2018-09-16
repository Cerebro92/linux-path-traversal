from base import BaseCommand

class CDCommand(BaseCommand):
    def __init__(self, directory):
        self.directory = directory

    def run(self, new_directory):
        # Find directory by name
        # set current directory to new directory
        self.directory = self.directory.find_subdirectory_by_name(new_directory)
