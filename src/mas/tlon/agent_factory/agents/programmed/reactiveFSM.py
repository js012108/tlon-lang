from mas.tlon.agent_factory.abstract_agent import *
from mas.tlon.agent_factory.behaviors import *

"""Agent example transitioning betweeen letters without any particular reason, like life itself """

class AbcFSM(AbstractAgent):

    class Periodic(PeriodicBehaviour):

        def on_start(self):
            logging.info("Starting behaviour . . .")
            self.counter = 0

        def _on_tick(self):
            logging.info("Counter: {}".format(self.counter))
            #print('counter ', self.counter)
            self.counter = self.counter + 1

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting FSM . . .")

        def on_end(self):
            print("Ending FSM . . .")

        def fsm_action(self):
            #self.ordered_transitions(['c','b','a'])
            #self.run_with_timer(2,10)
            self.perceive_text_input()

    def _setup(self):
        states = ['a','b','c']
        transitions = [{'trigger':'atob','source':'a','dest':'b'},
                        {'trigger':'btoc','source':'b','dest':'c'},
                        {'trigger':'ctoa','source':'c','dest':'a'}]
        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        b = self.Periodic(0.1, 10)
        self.add_behaviour(b)
        fsm_behaviour.start()
        b.start()
        b.join()
        fsm_behaviour.join()


""" Agent that controls the on and off system off a fridge depending on a temperature sensor and user defined upper and lower boundaries """
class FridgeFSM(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting Fridge behavior . . .")

        def on_end(self):
            print("Ending Fridge behavior . . .")

    def _setup(self):
        states = ['turn_on','turn_off']
        transitions = [
            { 'trigger': 'high_temperature', 'source': 'turn_off', 'dest': 'turn_on' },
            { 'trigger': 'temperature_is_fine', 'source': 'turn_on', 'dest': 'turn_off'}
        ]
        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        fsm_behaviour.start()
        fsm_behaviour.join()


""" Agent in charge of deploy new bets """

class Dealer(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting dealer behavior as FSM ...")

        def on_end(self):
            print("Ending dealer behavior as FSM ...")

    def _setup(self):

        states =['Configuracion','ConsultarWS','CreacionApuesta']
        transitions = [
            { 'trigger': 'FConfiguracion', 'source': 'Configuracion', 'dest': 'ConsultarWS' },
            { 'trigger': 'NadaNuevo', 'source': 'ConsultarWS', 'dest': 'ConsultarWS'},
            { 'trigger': 'NuevaApuesta', 'source': 'ConsultarWS', 'dest': 'CreacionApuesta' },
            { 'trigger': 'BuscarOtra', 'source': 'CreacionApuesta', 'dest': 'ConsultarWS' }
        ]
        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        fsm_behaviour.start()
        fsm_behaviour.join()

""" Agent in charge of take new bets and open them to the public """

class BetOpener(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting BetOpener behavior as FSM . . .")

        def on_end(self):
            print("Ending BetOpener behavior as FSM. . .")

    def _setup(self):

        states=['NuevaApuesta','PublicarConfigurar','AbrirApuesta']
        transitions = [
            { 'trigger': 'RecibeApuesta', 'source': 'NuevaApuesta', 'dest': 'PublicarConfigurar' },
            { 'trigger': 'ApuestaConfigurada', 'source': 'PublicarConfigurar', 'dest': 'AbrirApuesta'},
            { 'trigger': 'ApuestaAbierta', 'source': 'AbrirApuesta', 'dest': 'NuevaApuesta' },
            { 'trigger': 'EApuesta', 'source': 'NuevaApuesta', 'dest': 'NuevaApuesta' }
        ]
        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        fsm_behaviour.start()
        fsm_behaviour.join()

""" Agent that observe a group of bets waiting to process the clossing """

class BetCloser(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting BetCloser behavior as FSM . . .")

        def on_end(self):
            print("Ending BetCloser behavior as FSM. . .")

    def _setup(self):

        states=['BuscarACierre','Actualizar','ComunicarJugadores']
        transitions = [
            { 'trigger': 'ApuestaPorCerrar', 'source': 'BuscarACierre', 'dest': 'Actualizar' },
            { 'trigger': 'Consolidado', 'source': 'Actualizar', 'dest': 'ComunicarJugadores'},
            { 'trigger': 'EnCola', 'source': 'ComunicarJugadores', 'dest': 'ComunicarJugadores' },
            { 'trigger': 'NadaNuevo', 'source': 'BuscarACierre', 'dest': 'BuscarACierre' }
        ]
        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        fsm_behaviour.start()
        fsm_behaviour.join()

""" Agent that pays bets in a online casino enviroment """

class BetPayer(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting BetPlayer behavior as FSM . . .")

        def on_end(self):
            print("Ending BetPlayer behavior as FSM. . .")

    def _setup(self):

        states=['Espera','Contabilidad','Paga']
        transitions = [
            { 'trigger': 'NadaNuevo', 'source': 'Espera', 'dest': 'Espera' },
            { 'trigger': 'CierreRecibido', 'source': 'Espera', 'dest': 'Contabilidad'},
            { 'trigger': 'AjustesEnCola', 'source': 'Contabilidad', 'dest': 'Contabilidad'},
            { 'trigger': 'NumListos', 'source': 'Contabilidad', 'dest': 'Paga' },
            { 'trigger': 'PagosEnCola', 'source': 'Paga', 'dest': 'Paga' }
        ]
        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        fsm_behaviour.start()
        fsm_behaviour.join()

#Agent capable of recognize a chain string

class FiniteStateMachine(FSM):

    def on_start(self):
        print("Starting FSM ...")

    def on_end(self):
        print("Endng FSM ...")

class OneStringDetector(AbstractAgent):

    def __init__(self, description, jid, password,string='', community_id=''):
        AbstractAgent.__init__(self,description, jid, password, community_id)
        self.string = string
        self.states = []
        self.transitions = []
        self.fsm = None

    def generate_transitions(self):
        if  self.string:
            self.states=list(self.string)
            self.transitions = []
            i = 0
            while (i<len(self.states)-1):
                trigger = self.states[i]+"to"+self.states[i+1]
                transition = { 'dest':self.states[i+1], 'source':self.states[i], 'trigger':trigger}
                self.transitions.append(transition)
                i += 1
        else:
            print("Can't generate FSM from an empty string")


    #Return true if given string is the same as the stored one
    def validateString(self, text):
        i=0
        while(i<len(text)-1):
            try:
                eval('self.fsm.'+text[i]+'to'+text[i+1]+'()')
            except:
                print("Letter " + text[i+1] + " after letter " + text[i] + " is not recognized by this agent")
                return
            i += 1

    #Change the stored string
    def updateString(self):
        TODO

    def _setup(self):
        transitions = self.generate_transitions()
        self.fsm = FiniteStateMachine(states=self.states, transitions=self.transitions, initial=self.states[0])
        self.add_behaviour(self.fsm)
        self.fsm.start()
        self.fsm.join()
