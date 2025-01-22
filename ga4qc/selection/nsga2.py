from deap.tools.emo import selNSGA2
from deap.base import Fitness as DeapFitness
from random import choice
from typing import List, Tuple, Dict

from ga4qc.circuit import Circuit
from .interface import ISelection


class DeapWrapper:
    fitness: DeapFitness
    circuit: Circuit

    def __init__(self, circuit: Circuit):
        self.circuit = circuit

        DeapFitness.weights = tuple([-1 for _ in circuit.fitness_values])
        self.fitness = DeapFitness(values=circuit.fitness_values)

    def unwrap(self) -> Circuit:
        return self.circuit


class NSGA2(ISelection):
    def __init__(self):
        pass

    def select(self, circuits: List[Circuit], k: int) -> List[Circuit]:
        wrapped_circuits: List[DeapWrapper] = [
            DeapWrapper(circuit) for circuit in circuits
        ]

        selection: List[DeapWrapper] = selNSGA2(individuals=wrapped_circuits, k=k)

        selection: List[Circuit] = [
            wrapped_circuit.unwrap() for wrapped_circuit in selection
        ]
        return selection
