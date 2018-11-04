import time
import datetime
from random import randint
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message


class VoterAgent(Agent):
    class VoteBehav(OneShotBehaviour):
        async def run(self):
            while len(self.judgment)<2:
                msg = await self.receive(timeout=5)
                if msg:
                    self.judgment.append(msg.body.split('_'))
                else:
                    print("Did not received any message after 5 seconds")
                    self.kill()
            decision = 0
            body_vote = ''
            for candidate in self.judgment:
                if int(candidate[1])/int(candidate[2]) > decision:
                    decision = int(candidate[1])/int(candidate[2])
                    body_vote = candidate[0]
            msg = Message(to="veedor@localhost")  # Instantiate the message
            msg.body = str(body_vote)
            msg.set_metadata("subject", "continue")
            
            while self._gateway==None:
                await self.send(msg)
                msg = await self.receive(timeout=10)
                if msg:
                    if msg.metadata['subject'] == 'election':
                        self._gateway = msg.body
                        print("==========GATEWAY=======", self._gateway)
                else:
                    print("Did not received any message after 10 seconds")
                    self.kill()
            
            self.agent.stop()

        async def on_end(self):
            # stop agent from behaviour
            self.agent.stop()

        async def on_start(self):
            self.judgment = []
            self._gateway = None

    def setup(self):
        b = self.VoteBehav()
        self.add_behaviour(b)


class CandidateAgent(Agent):
    class CampBehav(OneShotBehaviour):
        def __init__(self, jid):
            OneShotBehaviour.__init__(self)
            self.jabid = jid
        
        async def run(self):
            time.sleep(10)
            for voter in self.voters:
                body = str(self.jabid) + '_' + str(self.resources) + '_' + str(randint(1,10))
                msg = Message(to=voter)  # Instantiate the message
                msg.body = body
                msg.set_metadata("subject", "continue")
                await self.send(msg)
            self.agent.stop()

        async def on_end(self):
            self.agent.stop()
        
        async def on_start(self):
            self.resources = randint(1,10)*10
            self.voters = ['voter1@localhost','voter2@localhost', 'voter3@localhost', 'voter4@localhost', 'voter5@localhost']
            print("Resources",self.jabid, self.resources)

    def setup(self):
        b = self.CampBehav(self.jid)
        self.add_behaviour(b)

class VeedorAgent(Agent):
    class CountBehav(OneShotBehaviour):        
        async def run(self):
            while self.active_voters<5:
                msg = await self.receive(timeout=5)
                if msg:
                    self.candidates[msg.body] += 1
                    self.active_voters += 1
                else:
                    print("Did not received any message after 5 seconds")
                    self.kill()
            print(self.candidates)
            gateway = max(self.candidates,key=self.candidates.get)
            for voter in self.voters:
                body = gateway
                msg = Message(to=voter)  # Instantiate the message
                msg.body = body
                msg.set_metadata("subject", "election")
                await self.send(msg)


        async def on_end(self):
            self.agent.stop()
        
        async def on_start(self):
            self.candidates = {'candidate1@localhost':0, 'candidate2@localhost':0}
            self.voters = ['voter1@localhost','voter2@localhost', 'voter3@localhost', 'voter4@localhost', 'voter5@localhost']
            self.active_voters = 0

    def setup(self):
        b = self.CountBehav()
        self.add_behaviour(b)

if __name__ == "__main__":
    voter1 = VoterAgent("voter1@localhost", "pass123")
    voter2 = VoterAgent("voter2@localhost", "pass123")
    voter3 = VoterAgent("voter3@localhost", "pass123")
    voter4 = VoterAgent("voter4@localhost", "pass123")
    voter5 = VoterAgent("voter5@localhost", "pass123")
    voters = [voter1, voter2, voter3, voter4, voter5]

    candidate1 = CandidateAgent("candidate1@localhost", "pass123")
    candidate2 = CandidateAgent("candidate2@localhost", "pass123")
    candidates = [candidate1, candidate2]

    veedor = VeedorAgent("veedor@localhost", "pass123")

    for candidate in candidates:
        candidate.start()
    
    veedor.start()

    for voter in voters:
        voter.start()



    while veedor.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            for candidate in candidates:
                candidate.stop()
            for voter in voters:
                voter.stop()
            veedor.stop()
            break
    print("Agents finished")