from mas.tlon.agent_factory.abstract_agent import *
from mas.tlon.agent_factory.behaviors import *


class CycleAgent(AbstractAgent):

    class Periodic(PeriodicBehaviour):

        def on_start(self):
            logging.info("Starting behaviour . . .")
            self.counter = 0

        def _on_tick(self):
            logging.info("Counter: {}".format(self.counter))
            #print('counter ', self.counter)
            self.counter = self.counter + 1

    def _setup(self):
        b = self.Periodic(1, 10)
        self.add_behaviour(b)
        b.start()
        b.join()

