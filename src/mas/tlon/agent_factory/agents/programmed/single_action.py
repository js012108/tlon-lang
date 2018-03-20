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
        self.behavior = PingServer(hostname)

    def _setup(self):
        behaviour = self.behavior
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()

"""Agent that executes humidity and temperature measurement from python2"""

class ExecuteScript(OneShotBehavior):

    def __init__(self, script):
        OneShotBehavior.__init__(self)
        self.script = script

    def _single_action(self):
        response = os.system("python " + "test/" + self.script)
        print(response)

class MeasurementAgent(AbstractAgent):
    
    def __init__(self,  identifier, description ):
        AbstractAgent.__init__(self, identifier, description)
        self.behaviour = ExecuteScript("scripts/measure_taker.py")
    
    def _setup(self):
        self.add_behaviour(self.behaviour)
        self.behaviour.start()
        self.behaviour.join()


