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

    def _init_(self, hostname):
        OneShotBehavior._init_(self)
        self.hostname = hostname

    def _single_action(self):
        response = os.system("ping -c 1 " + self.hostname)
        if response == 0:
            print(self.hostname, 'is up!')
        else:
            print(self.hostname, 'is down!')

class PingAgent(AbstractAgent):

    def _init_(self,  identifier, description, hostname):
        AbstractAgent._init_(self, identifier, description)
        self.behavior1 = PingServer(hostname=hostname)

    def _setup(self):
        behaviour = self.behavior1
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()