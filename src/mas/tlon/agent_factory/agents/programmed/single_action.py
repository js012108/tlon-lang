from mas.tlon.agent_factory.abstract_agent import *
from mas.tlon.agent_factory.behaviors import *
import os

class SingleActionAgent(AbstractAgent):

    class AnAction(OneShotBehavior):

        def _single_action(self):
            logging.info('I am a single action agent!')

    def _setup(self):
        b = self.AnAction()
        self.add_behaviour(b)
        b.start()
        b.join()

class PingServer(OneShotBehavior):

    def __init__(self, hostname):
        OneShotBehavior.__init__(self)
        self.hostname = hostname

    def _single_action(self):
        response = os.system("ping -c 1 " + self.hostname)
        if response == 0:
            print(self.hostname, 'is up!')
        else:
            print(self.hostname, 'is down!')

class PingAgent(AbstractAgent):

    def __init__(self,  identifier, description, hostname):
        AbstractAgent.__init__(self, identifier, description)
        self.behavior1 = PingServer(hostname)

    def _setup(self):
        behaviour = self.behavior1
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()
