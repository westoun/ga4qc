from typing import List

from ga4qc.circuit import Circuit
from ga4qc.fitness import IFitness
from ga4qc.simulator import ISimulator

from .interface import ICircuitProcessor


class CircuitEvaluator(ICircuitProcessor):
    """Circuit processor that handles the simulation of
    a population of circuits as well as their fitness
    evaluation."""

    fitness: IFitness
    simulator: ISimulator

    def __init__(self, fitness: IFitness, simulator: ISimulator):
        self.fitness = fitness
        self.simulator = simulator

    def process(self, circuits: List[Circuit]) -> None:
        self.simulator.simulate(circuits)
        self.fitness.score(circuits)
