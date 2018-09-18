from cmds.base import BaseCommand
from entity.directory import DirectoryEntity
from state import current_state

class SESSIONCommand(BaseCommand):
    @classmethod
    def run(cls, action):
        current_state.take_me_home()
        current_state.take_me_to_dir(DirectoryEntity(""))
        return True, "RESET TO HOME!"
