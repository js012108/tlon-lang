
from functools import wraps
from random import randint
import abc

COOP = 'cooperate'
DEF = 'defeat'


class AbstractStrategy(object):

    pass

#####################################################################


def cooperate():
    return 1


def defeat():
    return 0


def swap(val):
    return 1 - val


def random(threshold):
    return cooperate() if randint(0, 9) >= threshold else defeat()


class AbstractStrategy(object):

    pass

#####################################################################


class Strategy:
    """Abstract Base Class which stores state (last and second last plays)."""
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._last_play = self._last_rs = self._last_second_play = 1

    @abc.abstractmethod
    def decide(self, rs):
        """Returns the next play (cooperate or defeat) based on the own state
        and the opponent's play in the last iteration."""
        return

    @staticmethod
    def default(play):
        """Overrides arg of the decorated function if it is None."""
        def decorate(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                if args[1] is None:
                    largs = list(args)
                    largs[1] = cooperate() if play is COOP else defeat()
                    return fn(*tuple(largs), **kwargs)
                else:
                    return fn(*args, **kwargs)
            return wrapper
        return decorate

    @staticmethod
    def record(fn):
        """Keeps track of the last decission."""
        @wraps(fn)
        def wrapper(*args, **kwargs):
            _aux = args[0]._last_play
            args[0]._last_play = fn(*args, **kwargs)
            args[0]._last_second_play = _aux
            if args[1] is not None:
                args[0]._last_rs = args[1]
            return args[0]._last_play
        return wrapper


class Nice(Strategy):
    """Cooperates (almost) always."""
    def decide(self, _):
        return cooperate() if random(3) else defeat()


class Naive(Strategy):
    """Repeats the last play if the opponent cooperated."""
    @Strategy.default(COOP)
    @Strategy.record
    def decide(self, rs):
        return self._last_play if rs else swap(self._last_play)


class NaiveProber(Strategy):
    """Defeats with 20% chance, else repeats the last play if the opponent cooperated."""
    @Strategy.default(DEF)
    @Strategy.record
    def decide(self, rs):
        if random(8):
            return defeat()
        else:
            return self._last_play if rs else swap(self._last_play)


class Crazy(Strategy):
    """Cooperates with 50% chance."""
    def decide(self, _):
        return random(5)


class TitForTat(Strategy):
    """Plays what the opponent played last time."""
    @Strategy.default(COOP)
    def decide(self, rs):
        return rs


class Selfish(Strategy):
    """Cooperates with 50% chance only if the opponent cooperated the last time."""
    @Strategy.default(DEF)
    def decide(self, rs):
        return rs and random(5)

