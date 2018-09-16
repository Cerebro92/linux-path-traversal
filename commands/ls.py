from commands.base import BaseCommand

class LSCommand(BaseCommand):
    def __init__(self, directory):
        self.directory = directory

    def run(self):
        print self.directory.subdirectories

