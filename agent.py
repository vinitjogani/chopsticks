import environment as env
import numpy as np


def rev(state):
    l, k, i, j = state
    return i, j, k, l


class Agent:
    def __init__(self):
        self.V = {}
        for state in env.states():
            self.V[state] = 0
        self.transitions = env.transitions()

    def best_action(self, state):
        state = env.sanitize(*state)
        choices = self.transitions[state]
        if not choices:
            return state
        return choices[np.argmin([self.V[env.sanitize(*rev(n))] for n in choices])]

    def train(self, n_iters=1000):
        for _ in range(n_iters):
            for state in env.states():
                self.update(state)

    def update(self, state):
        if state[0] == 0 and state[1] == 0:
            self.V[state] = -1
        elif state[2] == 0 and state[3] == 0:
            self.V[state] = 1

        max_a = self.best_action(state)
        max_a_opponent = rev(max_a)
        minimax_a_opponent = self.best_action(max_a_opponent)
        minimax_a = rev(minimax_a_opponent)
        v_next = self.V[env.sanitize(*minimax_a)]
        self.V[state] = 0.9 * v_next
