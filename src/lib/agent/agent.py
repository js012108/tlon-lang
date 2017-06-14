class State():
  id = None
  action = None
  input = None
  output = None
  acceptable = None
  transitions = []

  def __init__(self, id: int, action, acceptable: bool, transitions: []):
    self.id = id
    self.action = action
    self.acceptable = acceptable
    self.transitions = transitions

  def exec(self, param):
    self.output = self.action(param)
    return self.output

  def validateTransitions(self):
    for transition in self.transitions:
      if transition['condition'] == self.output:
        return transition['id']

    return None


class AbstractAgent():
  alphabet_in = []
  alphabet_out = []
  states = []

  def __init__(self, alphabet_in: [], alphabet_out: [], states: []):
    self.alphabet_in = alphabet_in
    self.alphabet_out = alphabet_out
    self.states = states


class Agent(AbstractAgent):

  name = None
  current_state = None

  def __init__(self, name: str, initial_state: int, states: []):
    super(self.__class__, self).__init__([], [], states)
    self.name = name

    current_state = list(filter(lambda x: x.id == initial_state, self.states))

    if len(current_state) > 1:
      raise Exception('More than one Initial State')
    elif len(current_state) == 0:
      raise Exception('No Initial State provided')

    self.current_state = current_state[0]

  def run(self):
    if not self.current_state:
      raise Exception('No current state set')

    input = None
    while True:
      result = self.current_state.exec(input)

      if self.current_state.acceptable == True:
        print ('Acceptable State: ' + str(self.current_state.id) + ' - ' + str(result))
        return result

      next_state = self.current_state.validateTransitions()
      input = result

      if next_state == None:
        raise Exception('No acceptable terminal state')

      current_state = list(filter(lambda x: x.id == next_state, self.states))
      if len(current_state) > 1:
        raise Exception('More than one State with ID ' + str(next_state))

      self.current_state = current_state[0]


'''

def action1(entrada):
  print('State 1: 10')
  return 10

def action2(entrada):
  print ('State 2: ' + str(entrada))
  return entrada

def action3(entrada):
  print ('State 3: ' + str(entrada))
  return entrada + 10

def action4(entrada):
  print('State 4: ' + str(entrada))
  return entrada

def action5(entrada):
  print('State 5: ' + str(entrada))
  return entrada

def main():
  state1 = State(1, action1, False, [
    { 'id': 2, 'condition': lambda x: x == 15 },
    { 'id': 3, 'condition': lambda x: x == 10 }
  ])
  state2 = State(2, action2, False, [])

  state3 = State(3, action3, False, [
    { 'id': 4, 'condition': lambda x: x == 30 },
    { 'id': 5, 'condition': lambda x: x == 20 }
  ])
  state4 = State(4, action4, False, [])
  state5 = State(5, action5, True, [])

  agent = Agent('Agente Suma', 1, False, [state1, state2, state3, state4, state5])

  result = agent.run()
  print ('RESULT: ' + str(result))


if __name__ == '__main__':
  main()
'''