from state import current_state
from cmds.base import BaseCommand
from entity.utils import serialize_dir

class LSCommand(BaseCommand):

    @classmethod
    def run(cls):
        """Get all subdirectories"""
        serialized = map(serialize_dir, current_state.current_dir.subdirectories)
        names = [s['name'] for s in serialized]
        return True, ' '.join(names)

    @classmethod
    def pretty_print(cls, status, response):
        if status:
            print "DIRS: %s" % response
        else:
            print "ERR: %s" % response

