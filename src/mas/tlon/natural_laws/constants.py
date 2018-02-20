
class Constants(object):

    def __init__(self):
        self.__PORT = 12345
        self.__BLOCK_SIZE = 8192
        self.__END_MARKER = '$\/.}<~&.*'
        self.__TIME_OUT = 10

    @property
    def port(self):
        return self.__PORT

    @property
    def block_size(self):
        return self.__BLOCK_SIZE

    @property
    def end_marker(self):
        return self.__END_MARKER

    @property
    def time_out(self):
        return self.__TIME_OUT
