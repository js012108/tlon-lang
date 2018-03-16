#Solo funciona con texto sin espacios y sin caracteres alfanumericos que no inicien con numeros
def generate_state_machine(text):
    states=list(text)
    transitions = []
    i = 0
    while (i<len(states)-1):
        trigger = states[i]+"to"+states[i+1]
        transition = { 'dest':states[i+1], 'source':states[i], 'trigger':trigger}
        transitions.append(transition)
        i += 1

def validate_text(text):
    for letter in text:
        eval(text[0]+"to"+"text[1]")

#El agente tiene que crear una maquina de estados y tiene que reconocer si una entrada es aceptable o no

generate_state_machine("abcdefg")