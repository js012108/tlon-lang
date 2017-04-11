import os

class FileManager():
    def __init__(self, path):
        self.file = None
        self.file_path = path

        file_name, file_type = os.path.splitext(path)
        self.filename = file_name[file_name.rfind('/'):]
        self.file_type = file_type

    def set_path(self, file_path):
        self.file_path = file_path

    def init_file(self, action):

        if action == 'r' and self.current_action == 'write' or action == 'w' and self.current_action == 'read':
            self.throw_exception('warning', 'ModeChangedWarning')

        if action == 'read':
            action = 'r'
            self.current_action = 'read'
        elif action == 'write':
            action = 'a'
            self.current_action = 'write'

        try:
            self.file = open(self.file_path, action)
        except Exception:
            self.throw_exception('error', 'NotFoundException')

        return self.file

    def get(self):
        if self.file_path is not None:

            self.init_file('read')
            data = self.file.readlines()
            data = list(map(lambda x: x.rstrip().strip(), data))
            return data

        else:
            self.throw_exception('error', 'NotFoundException')

    def get_line(self):
        if self.file_path is not None:

            self.init_file('read')

            return self.file.readline()
        else:
            self.throw_exception('error', 'NotFoundException')

    def put(self, data):
        if self.file_path is not None:

            self.init_file('write')
            out = str(data)

            if type(data) is not list:
                self.file.write("{}\n".format(out))
            else:
                data = map(lambda x: str(x) + '\n', data)
                self.file.writelines(data)

        else:
            self.throw_exception('NotFoundException')

    def close(self):
        if self.file is not None:
            self.file.close()
        else:
            self.throw_exception('error', 'NotFoundException')
        return True

    def throw_exception(self, type, code='Exception', message=None):
        if type == 'error':
            if code == 'NotFoundException':
                if message is None:
                    message = 'File not Found.'
                raise IOError(message)
            elif code == 'Exception':
                raise Exception(message)
            else:
                raise Exception(message)
        elif type == 'warning':
            if code == 'ModeChangedWarning':
                if message == None:
                    message = 'File Mode Changed'
                print('WARNING: ' + message)