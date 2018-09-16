from commands.base import BaseCommand

class RMCommand(BaseCommand):
    def __init__(self, directory):
        pass

    def run(self, name):
        _dir = self.directory.find_subdirectory_by_name(name)
        # delete from list
        self.directory.subdirectories.delete(_dir)

