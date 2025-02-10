from typing import List, Type

from ga4qc.circuit import Circuit, IGate, random_circuit
from .interface import ISeeder


class RandomSeeder(ISeeder):
    gate_set: List[Type[IGate]]
    gate_count: int
    qubit_num: int

    def __init__(self, gate_set: List[Type[IGate]], gate_count: int, qubit_num: int):
        self.gate_set = gate_set
        self.gate_count = gate_count
        self.qubit_num = qubit_num

    def seed(self, population_size: int) -> List[Circuit]:
        population = []

        for _ in range(population_size):
            circuit = random_circuit(self.gate_set, self.gate_count, self.qubit_num)
            population.append(circuit)

        return population
