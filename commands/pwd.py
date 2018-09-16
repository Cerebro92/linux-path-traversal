from commands.base import BaseCommand

class PWDCommand(BaseCommand):
    def __init__(self, directory):
        pass

    def run(self):
        path = []
        parent = self.directory.parent
        path.append(parent)

        while (parent):
            parent = parent.parent
            path.append(parent)

        return path[::-1]
