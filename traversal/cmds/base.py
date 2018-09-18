status_map = {
    True: 'SUCC',
    False: 'ERR'
}

class BaseCommand(object):

    @classmethod
    def run(cls):
        """To be implemented by subclasses"""
        raise NotImplementedError

    @classmethod
    def pretty_print(cls, status, response):
        print "%s: %s" % (status_map[status], response)
