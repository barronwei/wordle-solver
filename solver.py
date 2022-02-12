import random 
import pandas as pd

class Solver():
    def __init__(self, size, words, init):
        self.done = False
        self.size = size
        self.confirmed = size * [""]
        self.guesses = []
        self.hints = {}
        self.words = words
        self.init = init
    def debug(self):
        print("confirmed:", self.confirmed)
        print("guesses:", self.guesses)
        print("hints:", self.hints)
    def get_guesses(self):
        return self.guesses
    def get_next_step(self):
        for i, c in enumerate(self.confirmed):
            if c != "":
                self.words = list(filter(lambda x: x[i] == c, self.words))
        for k, v in self.hints.items():
            if len(v) != 0:
                for i in v:
                    self.words = list(filter(lambda x: x[i] != k, self.words))
                    self.words = list(filter(lambda x: k in x, self.words))
            else:
                self.words = list(filter(lambda x: k not in x, self.words))
        assert(len(self.words) != 0)
        return self.words[random.randint(0, len(self.words) - 1)]
    def validate_step(self, step, solution):
        self.guesses.append(step)
        for i, c in enumerate(step):
            if c == solution[i]:
                self.confirmed[i] = c
            else:
                if c not in self.hints.keys():
                    self.hints[c] = set() 
                if c in solution:
                    self.hints[c].add(i)
        self.done = step == solution or len(self.guesses) == self.size + 1
        return
    def step(self, solution):
        assert(len(solution) == self.size)
        if self.done:
            return
        next_step = self.init if len(self.guesses) == 0 else self.get_next_step()
        self.validate_step(next_step, solution)            
