import logging

import cmds
from state import current_state
from entity.directory import DirectoryEntity
from configs import setup_logging

setup_logging()

if __name__ == "__main__":
    print "Welcome to linux path traversal"
    print "Let me show you around"

    # setting up home location
    current_state.take_me_home()

    while True:
        _input = raw_input()
        splits = _input.split(" ")
        name, args = splits[0], splits[1:]

        try:
            __import__("cmds.{}".format(name))
        except ImportError as e:
            logging.warn("CANNOT RECOGNIZE INPUT - %s", name)
            continue

        try:
            module = getattr(cmds, name)
            klass = getattr(module, name.upper() + 'Command')
        except AttributeError as e:
            logging.warn("ERR: CANNOT RECOGNIZE INPUT - %s", name)
            continue

        try:
            response = klass.run(*args)
            logging.debug("Current dir - %s, command - %s, args - %s, response %s",
                          current_state.current_dir,
                          name, args, response)
            klass.pretty_print(*response)
        except Exception as e:
            logging.warn("ERR: INVALID PARAMS FOR COMMAND %s: %s", name, args)

