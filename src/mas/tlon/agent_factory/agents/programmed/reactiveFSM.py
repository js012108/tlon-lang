from mas.tlon.agent_factory.abstract_agent import *
from mas.tlon.agent_factory.behaviors import *
import requests

"""Agent example transitioning betweeen letters without any particular reason, like life itself """

class AbcFSM(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting FSM nihilist behaviour . . .")

        def on_end(self):
            print("Ending FSM nihilist behaviour . . .")

    def _setup(self):
        states = ['a','b','c']
        transitions = [{'trigger':'atob','source':'a','dest':'b'}]
        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        fsm_behaviour.start()
        fsm_behaviour.join()

""" Agent that controls the on and off system off a fridge depending on a temperature sensor and user defined upper and lower boundaries """
class FridgeFSM(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting Fridge behaviour . . .")

        def on_end(self):
            print("Ending Fridge behaviour . . .")

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
            print("Starting dealer behaviour as FSM ...")

        def on_end(self):
            print("Ending dealer behaviour as FSM ...")
    
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
            print("Starting BetOpener behaviour as FSM . . .")

        def on_end(self):
            print("Ending BetOpener behaviour as FSM. . .")
    
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
            print("Starting BetCloser behaviour as FSM . . .")

        def on_end(self):
            print("Ending BetCloser behaviour as FSM. . .")
    
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
            print("Starting BetPlayer behaviour as FSM . . .")

        def on_end(self):
            print("Ending BetPlayer behaviour as FSM. . .")
    
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


"""Agent capable of meassure temperature with a DHT11 sensor from a raspberry making samples and sending results to a webservice"""

class  HTDetector(AbstractAgent):

    def __init__(self, description, community_id='', ws='', pin=23):
        AbstractAgent.__init__(self, description, community_id)
        self.ws = ws
        self.pin = pin

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting HTDetector behaviour as FSM . . .")

        def on_end(self):
            print("Ending HTDetector behaviour as FSM. . .")
    
    """ Return true if OS of the host is raspbian """
    """ TODO """
    """ higly recommended create a general function for agents that return the host SO, is necessary for TLON proyect """
    def validate_os(self):
        try:
            import RPi.GPIO as gpio
            return True
        except:
            return False

    def configureDevice(self, ws):
        """Configure the device"""

    def _setup(self):
        if(self.validate_os()):
            #Verfiy if required libraries are installed in host
            try:
                import sys
                import time
                import Adafruit_DHT
                import requests
            except ImportError:
                print("One or more libraries can't be loaded")
 
            states=['Inicio','TomarMedida','EnviarMedida','Terminar']
            transitions = [
                { 'trigger': 'ConfiguracionTerminada', 'source': 'Inicio', 'dest': 'TomarMedida' },
                { 'trigger': 'ProcesadoConjunto', 'source': 'TomarMedida', 'dest': 'EnviarMedida' },
                { 'trigger': 'Apagar', 'source': 'Inicio', 'dest': 'Terminar' },
                { 'trigger': 'Apagar', 'source': 'TomarMedida', 'dest': 'Terminar' },
                { 'trigger': 'Apagar', 'source': 'EnviarMedida', 'dest': 'Terminar' },
                { 'trigger': 'MedirDeNuevo', 'source': 'EnviarMedida', 'dest': 'TomarMedida' },
                { 'trigger': 'ContinuarMidiendo', 'source': 'TomarMedida', 'dest': 'TomarMedida' }
            ]
            fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
            self.add_behaviour(fsm_behaviour)
            self.configureDevice(self.ws)

            try:
                self.sensor = Adafruit_DHT.DHT11
            except Exception:
                print("OS or libraries error")
            r = requests.post( ws, data={'number': 12524, 'type': 'issue', 'action': 'show'})
            print(r.status_code, r.reason)

            #Try to meassure temperature and humidity, then send it to ws
            try:
                while True:
                    humidity, temperature = Adafruit_DHT.read_retry(sensor, self.pin)
                    print('Temperature={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
                    r = requests.get( ws, data={'temp': temperature, 'hum': humidity})
                    print(r.status_code, r.reason)
                    time.sleep(10)

            except Exception:
                print("Error sending information to destiny service")

            fsm_behaviour.start()
            fsm_behaviour.join()

        else:
            print("The host device can´t run this function")


class ejemplo(AbstractAgent):

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("inicia ejemplo")

        def on_end(self):
            print("finaliza ejemplo")

    def si(self):
        print("si")

    def no(self):
        print("no")
    
    def _setup(self):
        
        states=['si','no']
        transitions = [
            { 'trigger': 'siano', 'source': 'si', 'dest': 'no', },
            { 'trigger': 'noasi', 'source': 'no', 'dest': 'si' }
        ]

        while(True):
            percepcion = input("What's your name? ")


        fsm_behaviour = self.FiniteStateMachine(states=states, transitions=transitions, initial=states[0])
        self.add_behaviour(fsm_behaviour)
        fsm_behaviour.start()
        fsm_behaviour.join()