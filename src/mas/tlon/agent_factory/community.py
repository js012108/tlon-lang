from .agents import *
import uuid

class Community():
    def __init__(self,dict_agents,assignment):
        self.dict_agents = dict_agents
        self.assignment = assignment
        self.agents = []

    def create(self):
        for agent in self.dict_agents:
            for number_agents in self.dict_agents[agent]:
                all_params = self.dict_agents[agent][number_agents]
                description = all_params["description"]
                jid = "agent"
                password="pass123"
                agent_type_params = all_params["params"]
                agent_type_params.insert(0,password)
                agent_type_params.insert(0,jid)
                agent_type_params.insert(0,description)
                for num in range(int(number_agents)):
                    agent_type_params[1]= jid+str(uuid.uuid4())[:8]
                    created_agent = eval(agent)(*agent_type_params)
                    self.agents.append(created_agent)
        return self.agents

    def start_agent(self,index):
        try:
            current_agent = self.agents[index]
            current_agent.start()
        except Exception as e:
            logging.info('[ERROR] community.start_agent() : {}'.format(e))
            sys.exit(0)
