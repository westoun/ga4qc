from random import choice
from typing import List

from ga4qc.circuit import Circuit
from .interface import ISelection


class TournamentSelection(ISelection):
    tourn_size: int

    def __init__(self, tourn_size: int = 2):
        self.tourn_size = tourn_size

    def select(self, circuits: List[Circuit], k: int, generation: int) -> List[Circuit]:
        selection = []

        for _ in range(k):
            contestors = [choice(circuits) for _ in range(self.tourn_size)]
            scores = [circuit.fitness_values[0] for circuit in contestors]
            min_score = min(scores)
            min_idx = scores.index(min_score)

            winner = contestors[min_idx]
            selection.append(winner.copy())

        return selection
