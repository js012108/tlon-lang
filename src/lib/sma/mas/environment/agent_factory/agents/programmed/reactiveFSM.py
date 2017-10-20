from mas.environment.agent_factory.abstract_agent import *
from mas.environment.agent_factory.behaviors import *

"""
#¿Que propiedades mantener?, si se mantienen actualizar en crear en creacion de fsm
#Crear método de agregar y eliminar estados y transiciones
"""

class ABCFSM(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting FSM behaviour . . .")

        def on_end(self):
            print("Ending FSM behaviour . . .")

    def _setup(self):
        states = ['a','b','c']
        transitions = [{'trigger':'atob','source':'a','dest':'b'}]
        b = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(b)
        b.start()
        b.join()