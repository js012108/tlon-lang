from mas.tlon.agent_factory.abstract_behavior import AbstractBehaviour
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
        AbstractBehaviour.__init__(self)
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
        
        logging.info('Behavior -FSM.{}- created successfully!'.
                     format(self.__class__.__name__))
        self.fsmActive = True
    
    #Report fsm stares and transitions
    def fsm_configuration(self):
        print(self._states)
        print(self._transitions)
    
    #Return actual state and action of the fsm
    def fsm_action(self):
        return self.state

    def _behave(self):
        self.fsm_action()
        return self._exit_code

    def done(self):
        if self.fsmActive is True:
            self.fsmActive = False
            return False
        return True

    def add_transition(self):
        pass

    #Add one or more states to fsm and return the new list of states
    def add_states(self, states):
        self._fsm.add_states(states)
        return self._fsm.states
    
    def remove_transition(self):
        pass

    def remove_states(self):
        pass

    def graph(self):
        pass

    def automaticRun(self, timeTransition):
        pass

