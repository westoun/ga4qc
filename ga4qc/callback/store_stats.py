from abc import ABC, abstractmethod

from statistics import mean, stdev
from typing import List, Callable


from ga4qc.circuit import Circuit
from .interface import ICallback


class StoreFitnessStats(ICallback, ABC):

    def __call__(self, circuits: List[Circuit], generation: int) -> None:
        fitness_scores = [circuit.fitness_values[0] for circuit in circuits]

        fit_mean = mean(fitness_scores)
        fit_best = min(fitness_scores)
        fit_worst = max(fitness_scores)
        fit_stdev = stdev(fitness_scores)

        self.store(fit_mean, fit_best, fit_worst, fit_stdev, generation)

    @abstractmethod
    def store(
        self,
        fit_mean: float,
        fit_best: float,
        fit_worst: float,
        fit_stdev: float,
        generation: int = None,
    ) -> None: ...
