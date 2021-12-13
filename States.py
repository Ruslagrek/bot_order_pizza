from transitions import Machine

class State_Machine(object):
    states = ['start_bot', 'pizza_size', 'payment_method', 'checking']


    def __init__(self, initial_state='start_bot'):
        self.machine = Machine(model=self, states=State_Machine.states, initial=initial_state)
        self.machine.add_ordered_transitions(self.states)
        self.machine.add_transition(trigger='cancel', source='*', dest='start_bot')