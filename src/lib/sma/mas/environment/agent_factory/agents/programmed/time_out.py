from mas.environment.agent_factory.abstract_agent import *

from mas.environment.agent_factory.behaviors import *


class TimeOutAgent(AbstractAgent):

    class TimeOutAction(TimeOutBehaviour):

        def time_out_action(self):

            logging.info('Hello, the timeout of {}s has ended!'.format(self.timeout))

    def _setup(self):
        b = self.TimeOutAction(5)
        self.add_behaviour(b)
        b.start()
        b.join()

