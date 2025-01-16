from abc import ABC, abstractmethod

from statistics import mean, stdev
from typing import List, Callable


from ga4qc.circuit import Circuit
from .interface import ICallback


class BestCircuitCallback(ICallback, ABC):

    def __call__(self, circuits: List[Circuit], generation: int) -> None:
        fitness_scores = [circuit.fitness_values[0] for circuit in circuits]

        best_fit = min(fitness_scores)
        min_idx = fitness_scores.index(best_fit)

        best_circuit = circuits[min_idx]

        self.handle(best_circuit, generation)

    @abstractmethod
    def handle(
        self,
        circuit: Circuit,
        generation: int = None,
    ) -> None: ...
