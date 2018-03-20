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

    def __init__(self, description, community_id='', string=''):
        AbstractAgent.__init__(self, description, community_id)
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
    
"""Agent capable of meassure temperature with a DHT11 sensor from a raspberry making samples and sending results to a webservice"""

class  HTDetector(AbstractAgent):

    def __init__(self, description, community_id='', ws='', pin=23):
        AbstractAgent.__init__(self, description, community_id)
        self.ws = ws
        self.pin = pin

    class FiniteStateMachine(FSM):

        def on_start(self):
            print("Starting HTDetector behavior as FSM . . .")

        def on_end(self):
            print("Ending HTDetector behavior as FSM. . .")
    
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



from platform import system as system_name
from os import system as system_call
import socket, datetime, gps, sys, time, Adafruit_DHT, requests

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
sensor = Adafruit_DHT.DHT11
pin = 23
lat = 0
lon = 0
time = 0

def gps():
    x = 1
    while x == 1:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print ('Hora:      ' + str(report.time))
                global time
                time = str(report.time)
            if hasattr(report, 'lat'):
                print ('Latitud:   ' + str(report.lat))
                global lat
                lat = str(report.lat)
            if hasattr(report, 'lon'):
                print ('Longitud:  ' + str(report.lon))
                global lon
                lon = str(report.lon)
            if hasattr(report, 'speed'):
                print ('Velocidad: ' + str(report.speed))
            if hasattr(report, 'track'):
                print ('Rumbo:     ' + str(report.track))
            if hasattr(report, 'head'):
                print (report.head)
            x= 0

try:
	# Ciclo principal infinito
	while True:
		humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
		gps()
		r = requests.post("http://www.bitsobet.com/maps/", data={'temp': temperatura, 'hum': humedad, 'longitud' : lon, 'latitud' : lat, 'humsuelo' : 0, 'precipitacion' : 6, 'datemed' : time})

# Se ejecuta en caso de que falle alguna instruccion dentro del try
except e:
	# Imprime en pantalla el error e
	print(str(e), "pos no")