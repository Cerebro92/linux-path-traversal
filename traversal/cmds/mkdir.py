from base import BaseCommand
from state import current_state
from entity.directory import DirectoryEntity

class MKDIRCommand(BaseCommand):

    @classmethod
    def run(self, name):
        """Create directory"""

        # check if already present
        _dir = current_state.current_dir.find_subdirectory_by_name(name)
        if _dir:
            return False, "DIRECTORY ALREADY EXISTS"

        # cerate new directory
        new_dir = DirectoryEntity(name, parent=current_state.current_dir)

        # Attach to file system
        current_state.current_dir.subdirectories.append(new_dir)

        return True, 'CREATED'

