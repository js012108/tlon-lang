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

class PingAgent(AbstractAgent):

	def __init__(self,  identifier, description, hostname):
		AbstractAgent.__init__(self, identifier, description)
		self.hostname = hostname

	def get_hostname(self):
		return self.hostname

	class PingServer(OneShotBehavior):

		def _single_action(self, hostname='google.com'):
			response = os.system("ping -c 1 " + hostname)
			if response == 0:
				print(hostname, 'is up!')
			else:
				print(hostname, 'is down!')

	def _setup(self):
		behaviour = self.PingServer()
		self.add_behaviour(behaviour)
		behaviour.start()
		behaviour.join()