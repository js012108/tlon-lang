import time
import datetime
import random
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour
from spade.message import Message


class ResourcesAgent(Agent):
    class ResourcesBehav(CyclicBehaviour):
        async def run(self):
            # msg.set_metadata("hey", "inform")
            if self.counter ==0:
                import time.sleep(10)
                msg = Message(to="testuser2@localhost")  # Instantiate the message
                msg.body = str(self.initial_resource)
                msg.set_metadata("subject", "continue")
                await self.send(msg)
                print("Negotiation start!")
            
            msg = await self.receive(timeout=5)
            if msg:
                if self.state_neg:
                    if self.counter == 10 and int(float(msg.body))==self.maximum_avaliable-1:
                        msg = Message(to="testuser2@localhost")  # Instantiate the message
                        msg.body = str(self.maximum_avaliable)
                        msg.set_metadata("subject", "last")
                        await self.send(msg)
                    elif msg.metadata['subject'] == 'finish':
                        print("==========NEGOTIATED RESOURCES=======", msg.body)
                        self.state_neg = False
                        self.kill()
                    elif msg.metadata['subject'] == 'last':
                        if int(float(msg.body)) > self.maximum_avaliable:
                            msg = Message(to="testuser2@localhost")  # Instantiate the message
                            msg.body = str(self.maximum_avaliable)
                            msg.set_metadata("subject", "last")
                            await self.send(msg)
                        else:
                            print("==========NEGOTIATED RESOURCES=======", msg.body)
                            self.state_neg = False
                            self.kill()
                    else:
                        new_resources = (int(float(msg.body)) + self.maximum_avaliable) / 2
                        if new_resources > self.maximum_avaliable:
                            msg = Message(to="testuser2@localhost")  # Instantiate the message
                            msg.body = str(self.maximum_avaliable)
                            msg.set_metadata("subject", "last")
                            await self.send(msg)
                        elif new_resources == self.maximum_avaliable:
                            print("==========NEGOTIATED RESOURCES=======", msg.body)
                            self.state_neg = False
                            self.kill()
                        else:
                            msg = Message(to="testuser2@localhost")  # Instantiate the message
                            msg.body = str(int(new_resources))
                            msg.set_metadata("subject", "continue")
                            await self.send(msg)
            else:
                print("Did not received any message after 5 seconds")
                self.kill()
            self.counter += 1

        async def on_end(self):
            # stop agent from behaviour
            self.agent.stop()

        async def on_start(self):
            self.counter = 0
            self.maximum_avaliable = random.randint(15, 50) #percentage
            self.initial_resource = random.randint(15,self.maximum_avaliable) #percentage
            self.state_neg = True
            print("RESOURCES ###### maximum ##### initial",self.maximum_avaliable,self.initial_resource)

    def setup(self):
        b = self.ResourcesBehav()
        self.add_behaviour(b)


class NetworkAgent(Agent):
    class NetBehav(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=5)  # wait for a message for 10 seconds
            if msg:
                # print("Message received with content: {}".format(msg.body))
                # print(msg.metadata)
                if self.state_neg:
                    if (msg.metadata)['subject'] == 'last':
                        if int(float(msg.body)) <= self.resources_needed and int(float(msg.body)) >= self.minimum_needed:
                            print("==========NEGOTIATED RESOURCES=======", msg['body'])
                            self.kill()
                        else:
                            print("==========NO AGREEMENT======= :C")
                            self.kill()
                        self.state_neg = False
                    else:
                        if int(float(msg.body)) >= self.resources_needed:
                            msg = Message(to="testuser1@localhost")
                            msg.set_metadata("subject", "finish")
                            msg.body = str(self.resources_needed)
                            await self.send(msg)
                        else:
                            new_resources = (int(float(msg.body)) + self.resources_needed) / 2
                            if new_resources >= self.minimum_needed:
                                msg = Message(to="testuser1@localhost")
                                msg.body = str(new_resources)
                                msg.set_metadata("subject", "continue")
                                await self.send(msg)
                            else:
                                msg = Message(to="testuser1@localhost")
                                msg.set_metadata("subject", "last")
                                msg.body = str(self.resources_needed)
                                await self.send(msg)
            else:
                print("Did not received any message after 5 seconds")
                self.kill()

        async def on_end(self):
            self.agent.stop()
        
        async def on_start(self):
            self.resources_needed = random.randint(15, 50) #percentage
            self.minimum_needed = self.resources_needed - random.randint(1,10) #percentage
            self.state_neg = True
            print("NETWORK ###### needed ##### minimum",self.resources_needed,self.minimum_needed)

    def setup(self):
        b = self.NetBehav()
        self.add_behaviour(b)


if __name__ == "__main__":
    receiveragent = NetworkAgent("testuser2@localhost", "pass123")
    receiveragent.start()
    time.sleep(1) # wait for receiver agent to be prepared. In next sections we'll use presence notification.
    senderagent = ResourcesAgent("testuser1@localhost", "pass123")
    senderagent.start()

    while receiveragent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            senderagent.stop()
            receiveragent.stop()
            break
    print("Agents finished")