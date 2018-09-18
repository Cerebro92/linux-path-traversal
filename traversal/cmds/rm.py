from state import current_state
from cmds.base import BaseCommand

class RMCommand(BaseCommand):
    @classmethod
    def run(cls, name_or_path):
        """Delete directory"""
        # keep a copy of current dir
        # need this to reset current location later
        current_dir = current_state.current_dir

        # if path is specified, go to that location first
        splits = name_or_path.rsplit("/", 1)
        is_path_specified = len(splits) == 2
        if is_path_specified:
            current_state.take_me_to_location(splits[0])
            dir_to_delete = splits[1]
        else:
            dir_to_delete = splits[0]

        # find directory to be deleted
        _dir = current_state.current_dir.find_subdirectory_by_name(dir_to_delete)
        if not _dir:
            return False, "INVALID PATH"

        # delete from list
        current_state.current_dir.subdirectories.remove(_dir)

        # Reset current location
        current_state.take_me_to_dir(current_dir)

        return True, "DELETED"

