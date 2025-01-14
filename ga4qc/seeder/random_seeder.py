from typing import List

from ga4qc.circuit import Circuit, GateSet
from .interface import ISeeder


class RandomSeeder(ISeeder):
    gate_set: GateSet

    def __init__(self, gate_set: GateSet):
        self.gate_set = gate_set

    def seed(self, population_size: int, gate_count: int) -> List[Circuit]:
        population = []

        for _ in range(population_size):
            circuit = self.gate_set.random_circuit(gate_count)
            population.append(circuit)

        return population
