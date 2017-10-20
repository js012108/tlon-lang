from mas.environment.agent_factory.abstract_behavior import AbstractBehaviour
from transitions import *
from transitions.extensions import GraphMachine
import threading
import logging

#####################################################################

class Reactive(AbstractBehaviour):
    pass

#####################################################################
class FSM(AbstractBehaviour):

    def __init__(self, states=[], transitions=[], initial='', graph=False, title=''):
        threading.Thread.__init__(self)
        self.setDaemon(False)
        self.my_owner = None
        self._force_kill = threading.Event()
        self.name = self.__class__.__name__
        self._exit_code = 0
        self._states = states
        self._transitions = transitions
        if  not graph:
            self._fsm = Machine(model=self, states=states, transitions=transitions, initial=initial)
        else:
            self._fsm = GraphMachine(model=self, states=states, transitions=transitions, initial=initial, title='title', show_conditions=True)
        AbstractBehaviour.__init__(self)
        logging.info('Behavior -FSM.{}- created successfully!'.
                     format(self.__class__.__name__))
        self.fsmActive = True
        
    def fsm_action(self):
        print(self._fsm.states)
        print(self._states)
        print(self._transitions)

    def _behave(self):
        self.fsm_action()
        return self._exit_code

    def done(self):
        if self.fsmActive is True:
            self.fsmActive = False
            return False
        return True