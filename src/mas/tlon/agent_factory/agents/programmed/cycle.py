import sys
sys.path.append('../../../..')
from mas.tlon.agent_factory.abstract_agent import AbstractAgent
from mas.tlon.agent_factory.behaviors import *
import subprocess


class CycleAgent(AbstractAgent):

    class Periodic(PeriodicBehaviour):

        def on_start(self):
            logging.info("Starting behaviour . . .")
            self.counter = 0

        def _on_tick(self):
            logging.info("Counter: {}".format(self.counter))
            self.counter = self.counter + 1

    def _setup(self):
        b = self.Periodic(1, 10)
        self.add_behaviour(b)
        b.start()
        b.join()


class CycleCallBash(AbstractAgent):

    class Periodic(PeriodicBehaviour):

        def on_start(self):
            logging.info("Starting behaviour . . .")
            self.counter = 0

        def _on_tick(self, command=["ls", "-l", "/dev/null"]):
            print(subprocess.run(command, stdout=subprocess.PIPE))
            self.counter = self.counter + 1

    def _setup(self):
        b = self.Periodic(1, 3)
        self.add_behaviour(b)
        b.start()
        b.join()
