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

    def __init__(self, description, jid, password,hostname, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
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

class MeasurementAgent(AbstractAgent):

    def __init__(self, description, jid, password, times, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.behaviour = ExecuteScript("scripts/measure_taker.py")
        self.times = times
        self.script = "scripts/measure_taker.py"

    def updateScript(self):
        with open('test/' + self.script, 'r') as file:
            data = file.readlines()
        data[0]='x = ' + str(self.times) + '\n'
        with open('test/' + self.script, 'w') as file:
            file.writelines( data )

    def _setup(self):
        self.updateScript()
        self.add_behaviour(self.behaviour)
        self.behaviour.start()
        self.behaviour.join()

'''Agent that vote '''
class VoteAction(OneShotBehavior):
    def __init__(self, veedor, Voter):
        OneShotBehavior.__init__(self)
        self.veedor = veedor + "@tlon"
        self.voter = Voter

    def _single_action(self):
        #import time
        #time.sleep(5)
        self.voter.send_message(mto=self.veedor,mbody="hola",mtype='chat')

class VoterAgent(AbstractAgent):
    def set_veedor(self,veedor):
        self.behaviour = VoteAction(veedor,self)

    def _setup(self):
        behaviour = self.behaviour
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()

'''Candidate agent'''

from random import randint
class CampaignAction(OneShotBehavior):
    def __init__(self, voters, Candidate):
        OneShotBehavior.__init__(self)
        self.voters = voters
        self.candidate = Candidate

    def _single_action(self):
        for voter in self.voters:
            print(voter.jabber_id,self.candidate.resources,randint(1,10))

class CandidateAgent(AbstractAgent):
    def __init__(self, description, jid, password, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.resources = randint(1,10)*10

    def set_voters(self, voters):
        self.behaviour = CampaignAction(voters,self)

    def _setup(self):
        behaviour = self.behaviour
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()
