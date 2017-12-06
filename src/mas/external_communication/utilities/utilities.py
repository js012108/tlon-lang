import json
import netifaces


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


#####################################################################

def dumps_json(fun):
    """
    Decorator to use json.dumps
    """
    def f(*args, **kwargs):
        return json.dumps(fun(*args, **kwargs))
    return f


#####################################################################

def loads_json(fun):
    """
    Decorator to use json.loads
    """
    def f(*args, **kwargs):
        return json.loads(fun(*args, **kwargs))
    return f


#####################################################################

def is_inet(inet):
    """
    Check if the tlon0 interface is avaiable
    """
    interface = False
    for i in netifaces.interfaces():
        if i == inet:
            interface = True
    return interface

#####################################################################


def is_batman_running(fun):
    """
    Decorator to check the B.A.T.M.A.N protocol
    """
    def f(*args, **kwargs):
        if is_inet('tlon0') or is_inet('bat0'):
            return fun(*args, **kwargs)
        else:
            return "[ERROR] B.A.T.M.A.N protocol is not running or tlon0 interface is not available!"
    return f