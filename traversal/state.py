"""
Implementation of singleton classes inspired from
https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
"""
import logging
from entity.directory import DirectoryEntity

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CurrentState(object):
    __metaclass__ = Singleton
    def __init__(self, current_dir=None):
        """
        singleton class to keep track of user's current location
        """
        logging.debug("Creating Singleton class current state")
        if not current_dir:
            current_dir = DirectoryEntity("")
        self.home = current_dir
        self.current_dir = current_dir

    def take_me_home(self):
        """Set current dir to home"""
        self.current_dir = self.home
        return True

    def take_me_at_absolute_location(self, dir_names):
        """Go to absolute path"""

        # Create a local copy of current_dir
        # so that we fails in finding destination
        # we can reset location to origin
        current_dir = current_state.current_dir
        current_state.take_me_home()

        has_moved = self.take_me_at_relative_location(dir_names)
        if not has_moved:
            current_state.current_dir = current_dir
            return False
        return True

    def take_me_at_relative_location(self, dir_names):
        """Go to relative location from current location"""
        current_dir = current_state.current_dir
        for dir_name in dir_names:
            current_dir = current_dir.find_subdirectory_by_name(dir_name)
            if not current_dir:
                return False

        current_state.current_dir = current_dir
        return True

    def take_me_to_location(self, name_or_path):
        """Go to a directory/absolute path"""

        if name_or_path == "/":
            status = self.take_me_home()
        elif name_or_path.startswith("/"):
            name_or_path = name_or_path[1:]
            dir_names = name_or_path.split("/")
            status = self.take_me_at_absolute_location(dir_names)
        else:
            dir_names = name_or_path.split("/")
            status = self.take_me_at_relative_location(dir_names)
        return status

    def take_me_to_dir(self, _dir):
        """Go to input directory"""
        self.current_dir = _dir


current_state = CurrentState()
