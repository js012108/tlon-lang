from tlon.communication.socket_methods import *
from tlon.resources import *
import sys
import random
import inspect
import multiprocessing


class AbstractAgent(multiprocessing.Process):
	"""
	Set of attributes and methods that  all agents in the system have
	no matter which behavior they exhibit
	"""

	def __init__(self, description, community_id=''):
		multiprocessing.Process.__init__(self)
		self.daemon = False
		self.community_id = community_id
		self.social_network = None
		self._name = self.__class__.__name__
		self._agent_id = random.randint(1, 100)
		self._description = description
		self._alive = True
		self._state = None
		self._running = False
		#self._force_kill
		#self._force_kill.clear()
		self._environment_id = random.random()
		self._default_behavior = None
		self._behaviour_list = dict()
		logging.info('Agent -{} created successfully!'.format(self.name))

	@property
	def agent_id(self):
		return self._agent_id

	@property
	def description(self):
		return self._description

	@property
	def name(self):
		return self._name

	@property
	def alive(self):
		return self._alive

	@property
	def environment_id(self):
		return self._name

	#####################################################################

	def perceive(self):
		pass

	#####################################################################

	def clone(self, address=get_ipv6_interface()):
		"""
	   Copy the agent's code and send it to another environment
		"""
		from mas.tlon import create_message
		from mas.tlon import Request
		logging.debug('clone method executed')
		try:
			agent_code = 'from mas.environment.agent_factory.abstract_agent import *\n\n' + '\n' + \
						 inspect.getsource(self.__class__)
		except Exception as e:
			print('[ERROR]' + e)
			sys.exit(1)

		data = list()
		data.append(self.name)
		data.append(agent_code)

		logging.info('Agent -{}- send to : {} '. format(data[0], address))
		return create_message(address, Request.CLONE, data)

	def environment_request(self, address, request, data):
		return create_message(address, request, data)

	def get_agent_info(self):
		return self.agent_id, self.community_id, self.description, self.state

	def dispersion(self):
		pass

	def get_code(self):
		return inspect.getsourcelines(self.__class__)

	def _setup(self):
		"""
		Configures the agent must be overridden
		"""
	pass

	def add_behaviour(self, behaviour):
		"""
		Adds a new behavior to the agent
		"""
		try:
			logging.debug('abstract_agent.add_behaviour() executed!')
			self._behaviour_list[behaviour.name] = ''
			behaviour.set_agent(self)
			logging.info('Behavior -{}- added to agent -{}-'.format(behaviour.name, self.name))
		except Exception as e:
			logging.info('[ERROR] abstract_agent.add_behavior() : {}'.format(e))
			sys.exit(0)

	def _register_agent(self):
		"""
		Register agent in the agent's directory
		"""
		return True

	def p2p_message(self):
		pass

	def community_message(self):
		pass

	def run(self):
		if self._register_agent():
			logging.info('Now agent -{}- is alive!'.format(self.name))
			self._setup()
			self._running = True
			logging.info('Now agent -{}- is inactive!'.format(self.name))

	#####################################################################
