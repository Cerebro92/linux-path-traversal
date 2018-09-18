import logging

from state import current_state
from cmds.base import BaseCommand

class PWDCommand(BaseCommand):

    @classmethod
    def run(cls):
        """
        Recursively check for parent directories, create a list
        Reverse that list to get path
        """
        path = []

        directory = current_state.current_dir
        while(directory):
            path.append(directory)
            directory = directory.parent

        # Reverse path
        ordered_path = path[::-1]

        # serialize in human readable format
        serialized_path = map(lambda x: x.serialize(), ordered_path)

        # fetch name from directory information
        file_names = [_dir['name'] for _dir in serialized_path]

        seperator = '/'
        path = None
        if file_names:
            path = seperator.join(file_names)

        if not path:
            path = seperator

        return True, path


    @classmethod
    def pretty_print(cls, status, response):
        if status:
            print "PATH: %s" % response
        else:
            print "ERR: %s" % response
