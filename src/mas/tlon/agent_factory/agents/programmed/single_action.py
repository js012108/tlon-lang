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
        #self.behaviour = ExecuteScript("scripts/measure_taker_dict.py")
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
        self.veedor = veedor + "@localhost"
        self.voter = Voter

    def _single_action(self):
        import time
        while len(self.voter.judgment)<len(self.voter.candidates):
            time.sleep(1)
        decision = 0
        body_vote = ''
        for candidate in self.voter.judgment:
            if int(candidate[1])/int(candidate[2]) > decision:
                decision = int(candidate[1])/int(candidate[2])
                body_vote = candidate[0]
        self.voter.send_message(mto=self.veedor,mbody=body_vote,mtype='chat')
        while (self.voter._gateway==None):
            time.sleep(1)

class VoterAgent(AbstractAgent):

    def __init__(self, description, jid, password, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.judgment = []
        self.candidates = []
        self._gateway = None

    def set_veedor(self,veedor):
        self.behaviour = VoteAction(veedor.jabber_id,self)
    
    def set_candidates(self, candidates_list):
        self.candidates = candidates_list

    def _setup(self):
        behaviour = self.behaviour
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()

    def message(self, msg):
        if msg['subject'] == 'election' and msg['type'] in ('chat', 'normal'):
            self._gateway = msg['body']
            print("voter_jabber_id", self.jabber_id, "==========GATEWAY=======", self._gateway)
        elif msg['type'] in ('chat', 'normal'):
            self.judgment.append(msg['body'].split('_'))

'''Candidate agent'''

from random import randint
class CampaignAction(OneShotBehavior):
    def __init__(self, voters, Candidate):
        OneShotBehavior.__init__(self)
        self.voters = voters
        self.candidate = Candidate

    def _single_action(self):
        import time
        time.sleep(8)
        for voter in self.voters:
            body = str(self.candidate.jabber_id) + '_' + str(self.candidate.resources) + '_' + str(randint(1,10))
            self.candidate.send_message(mto=voter.jabber_id+'@localhost',mbody=body,mtype='chat')

class CandidateAgent(AbstractAgent):
    def __init__(self, description, jid, password, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.resources = randint(1,10)*10
        print("Resources", self.resources)

    def set_voters(self, voters):
        self.behaviour = CampaignAction(voters,self)

    def _setup(self):
        behaviour = self.behaviour
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()

'''Veedor agent for elections (Registraduria)'''

class VoteCounterAction(OneShotBehavior):
    def __init__(self,Veedor):
        OneShotBehavior.__init__(self)
        self.counter_election = Veedor.candidates
        self.veedor = Veedor

    def _single_action(self):
        import time
        while sum(self.counter_election.values())<len(self.veedor.voters):
            time.sleep(1)
        gateway = max(self.counter_election,key=self.counter_election.get)
        print("==========RESULTS=======", self.counter_election)
        for voter in self.veedor.voters:
            self.veedor.send_message(mto=voter+'@localhost',mbody=gateway,msubject='election',mtype='chat')

class VeedorAgent(AbstractAgent):
    def __init__(self, description, jid, password, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.candidates = {}
        self.voters = []

    def set_candidates(self, candidates_list):
        for candidate in candidates_list:
            self.candidates[candidate.jabber_id] = 0

    def set_voters(self, voters_list):
        for voter in voters_list:
            self.voters.append(voter.jabber_id)

    def _setup(self):
        behaviour = VoteCounterAction(self)
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            self.candidates[msg['body']] += 1


'''Network Agent that will get resources in negotiation'''

import random
class NetworkAction(OneShotBehavior):
    def __init__(self,NetworkAgent):
        OneShotBehavior.__init__(self)
        self.network_agent = NetworkAgent

    def _single_action(self):
        import time
        while (self.network_agent.state_neg):
            time.sleep(1)

class NetworkAgent(AbstractAgent):
    def __init__(self, description, jid, password, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.resource_agent = None
        self.resources_needed = random.randint(15, 50) #percentage
        self.minimum_needed = self.resources_needed - random.randint(1,10) #percentage
        self.state_neg = True
        print("NETWORK ###### needed ##### minimum",self.resources_needed,self.minimum_needed)

    def set_resource_agent(self, resource_agent):
        self.resource_agent = resource_agent.jabber_id

    def _setup(self):
        behaviour = NetworkAction(self)
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()

    def message(self, msg):
        if msg['subject'] == 'last' and msg['type'] in ('chat', 'normal'):
            if int(float(msg['body'])) <= self.resources_needed and int(float(msg['body'])) >=self.minimum_needed:
                print("==========NEGOTIATED RESOURCES=======", msg['body'])
            else:
                print("==========NO AGREEMENT======= :C")
            self.state_neg = False
        elif msg['type'] in ('chat', 'normal'):
            if int(float(msg['body'])) >= self.resources_needed:
                self.send_message(mto=self.resource_agent+'@localhost',msubject='finish',mbody=str(self.resources_needed),mtype='chat')
                self.state_neg = False
            else:
                new_resources = (int(float(msg['body'])) + self.resources_needed) / 2
                if new_resources >= self.minimum_needed:
                    self.send_message(mto=self.resource_agent+'@localhost',mbody=str(int(new_resources)),mtype='chat')
                else:
                    self.send_message(mto=self.resource_agent+'@localhost',msubject='last',mbody=str(self.resources_needed),mtype='chat')
                    self.state_neg = False

'''Resources Agent that will give resources in negotiation'''

import random
class ResourcesAction(OneShotBehavior):
    def __init__(self, ResourceAgent):
        OneShotBehavior.__init__(self)
        self.resource_agent = ResourceAgent

    def _single_action(self):
        network = self.resource_agent.network
        resources = str(self.resource_agent.initial_resource)
        self.resource_agent.send_message(mto=network+'@localhost',mbody=resources,mtype='chat')
        import time
        while (self.resource_agent.state_neg):
            time.sleep(1)

class ResourcesAgent(AbstractAgent):
    def __init__(self, description, jid, password, community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.network = None
        self.maximum_avaliable = random.randint(15, 50) #percentage
        self.initial_resource = random.randint(15,self.maximum_avaliable) #percentage
        self.counter = 0
        self.state_neg = True
        print("RESOURCES ###### maximum ##### initial",self.maximum_avaliable,self.initial_resource)

    def set_network(self,network):
        self.network = network.jabber_id

    def _setup(self):
        behaviour = ResourcesAction(self)
        self.add_behaviour(behaviour)
        behaviour.start()
        behaviour.join()

    def message(self, msg):
        self.counter += 1
        if self.counter == 10 and int(float(msg['body']))==self.maximum_avaliable-1:
            self.send_message(mto=self.network+'@localhost',msubject='last',mbody=str(self.maximum_avaliable),mtype='chat')
            self.state_neg = False
        elif msg['subject'] == 'finish' and msg['type'] in ('chat', 'normal'):
            print("==========NEGOTIATED RESOURCES=======", msg['body'])
            self.state_neg = False
        elif msg['subject'] == 'last' and msg['type'] in ('chat', 'normal'):
            if int(msg['body']) > self.maximum_avaliable:
                self.send_message(mto=self.network+'@localhost',msubject='last',mbody=str(self.maximum_avaliable),mtype='chat')
            else:
                print("==========NEGOTIATED RESOURCES=======", msg['body'])
            self.state_neg = False
        else:
            new_resources = (int(float(msg['body'])) + self.maximum_avaliable) / 2
            if new_resources > self.maximum_avaliable:
                self.send_message(mto=self.network+'@localhost',msubject='last',mbody=str(self.maximum_avaliable),mtype='chat')
                self.state_neg = False
            elif new_resources == self.maximum_avaliable:
                print("==========NEGOTIATED RESOURCES=======", msg['body'])
                self.state_neg = False
            else:
                self.send_message(mto=self.network+'@localhost',mbody=str(int(new_resources)),mtype='chat')
