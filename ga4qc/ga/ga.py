from typing import List

from ga4qc.mutation import IMutation
from ga4qc.crossover import ICrossover
from ga4qc.simulator import ISimulator
from ga4qc.circuit import Circuit, GateSet
from ga4qc.fitness import IFitness
from ga4qc.circuit_processor import ICircuitProcessor
from ga4qc.selection import ISelection
from ga4qc.seeder import ISeeder


class GA:

    seeder: ISeeder
    mutations: List[IMutation]
    crossovers: List[ICrossover]
    circuit_processors: List[ICircuitProcessor]
    selection: ISelection

    def __init__(
        self,
        seeder: ISeeder,
        mutations: List[IMutation],
        crossovers: List[ICrossover],
        circuit_processors: List[ICircuitProcessor],
        selection: ISelection,
    ):
        # TODO: Add default values for unspecified
        # operators.
        self.seeder = seeder
        self.mutations = mutations
        self.crossovers = crossovers
        self.circuit_processors = circuit_processors
        self.selection = selection

    def run(self, population_size: int, gate_count: int, generations: int):
        population = self.seeder.seed(population_size, gate_count)

        raise NotImplementedError()
        for generation in range(1, generations):
            pass
