def fn(text):
    states=list(text)
    transitions = []
    i = 0
    while (i<len(states)-1):
        trigger = states[i]+"to"+states[i+1]
        transition = { 'dest':states[i+1], 'source':states[i], 'trigger':trigger}
        transitions.append(transition)
        print(trigger)
        print(transition)
        i += 1
    print(transitions)

    

fn("abcdefg")