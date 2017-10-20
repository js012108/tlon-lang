import time
import logging
from mas.environment.agent_factory.abstract_behavior import AbstractBehaviour


class OneShotBehavior(AbstractBehaviour):
    """
    This behavior is only executed once. This model was based in
    the SPADE behaviors library. You can check it in https://pypi.python.org/pypi/SPADE
    """
    def __init__(self):
        AbstractBehaviour.__init__(self)
        self._first_time = True
        self.name = self.__class__.__name__
        logging.info('Behavior -reflex.{}- created successfully!'.
                     format(self.__class__.__name__))

    def _single_action(self):
        pass

    def _behave(self):
        self._single_action()
        return self._exit_code

    def done(self):
        if self._first_time is True:
            self._first_time = False
            return False
        return True

############################################################


class PeriodicBehaviour(AbstractBehaviour):
    """
    This behavior runs periodically with a period. This model was taken of
    the SPADE behaviors library. You can check it in https://pypi.python.org/pypi/SPADE
    """

    def __init__(self, period, iterations=float("inf"), time_start=None):
        AbstractBehaviour.__init__(self)
        self.name = self.__class__.__name__
        self._period = period
        self._iterations = iterations
        self._temp = 0

        if time_start is None:
            self._next_activation = time.time()
        else:
            self._next_activation = time_start
        logging.info('Behavior -reflex.{}- created successfully!'.format(str(self.__class__.__name__)))

    def period(self):
        return self._period

    def set_period(self, period):
        self._period = period

    def _behave(self):

        if time.time() >= self._next_activation and (self._temp < self._iterations):
            self._exit_code = self._on_tick()

            while self._next_activation <= time.time():
                self._next_activation += self._period
            self._temp = self._temp + 1

        elif not self._temp < self._iterations:
            self.is_done = True
        else:
            t = self._next_activation - time.time()
            if t > 0:
                time.sleep(t)
        return self._exit_code

    def _on_tick(self):
        """
        This method is executed every period must be overridden
        """
        raise NotImplementedError

############################################################


class TimeOutBehaviour(PeriodicBehaviour):

    """
    This behavior is executed only once after a timeout. This model was taken of
    the SPADE behaviors library. You can check it in https://pypi.python.org/pypi/SPADE
    """
    def __init__(self, timeout):
        self._timeout = timeout
        PeriodicBehaviour.__init__(self, timeout, float("inf"), time.time() + self._timeout)
        self.name = self.__class__.__name__

    @property
    def timeout(self):
        return self._timeout

    def _on_tick(self):
        self.time_out_action()
        self.is_done = True

    def time_out_action(self):
        """
        This method is executed after the timeout must be overridden
        """
        raise NotImplementedError
