from base import BaseCommand
from state import current_state

class CDCommand(BaseCommand):
    @classmethod
    def run(cls, name_or_path):
        status = current_state.take_me_to_location(name_or_path)
        if status:
            return True, 'REACHED'
        else:
            return False, "INVALID PATH"

