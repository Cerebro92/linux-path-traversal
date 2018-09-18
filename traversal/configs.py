
import signal
import sys
import yaml
import logging
import logging.config

def setup_logging():
    logging.config.dictConfig(yaml.load(open('logging_config.yaml', 'r')))

def signal_handler(signal, frame):
    print('Good bye!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
