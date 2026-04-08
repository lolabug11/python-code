class StateNotFound(Exception):
    def __init__(self, state):
        super().__init__(f'{state} is not a valid state')
class ActionNotValid(Exception):
    def __init__(self, state, action):
        super().__init__(f'{action} is not a valid action for {state}')

class States:
    def __init__(self, starting_state):
        self.states = {starting_state: {}}
        self.current_state = starting_state

    def __str__(self):
        return f'The current state is {self.current_state}'

    def add_state(self, new_state_name):
        self.states[new_state_name] = {}

    def add_transition(self, state, action, next_state):
        if state not in self.states :
            raise StateNotFound(state)
        elif next_state not in self.states:
            raise StateNotFound(next_state)
        self.states[state][action] = next_state

    def trigger(self, action):
        if action not in self.states[self.current_state]:
            raise ActionNotValid(self.current_state, action)
        self.current_state = self.states[self.current_state][action]