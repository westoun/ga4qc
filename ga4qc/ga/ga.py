import random
from typing import List

from ga4qc.mutation import IMutation
from ga4qc.crossover import ICrossover
from ga4qc.circuit import Circuit, GateSet
from ga4qc.processors import ICircuitProcessor
from ga4qc.selection import ISelection
from ga4qc.seeder import ISeeder
from ga4qc.callback import ICallback


class GA:

    seeder: ISeeder
    mutations: List[IMutation]
    crossovers: List[ICrossover]
    processors: List[ICircuitProcessor]
    selection: ISelection

    after_generation_callbacks: List[ICallback]

    def __init__(
        self,
        seeder: ISeeder,
        mutations: List[IMutation],
        crossovers: List[ICrossover],
        processors: List[ICircuitProcessor],
        selection: ISelection,
    ):
        # TODO: Add default values for unspecified
        # operators.
        self.seeder = seeder
        self.mutations = mutations
        self.crossovers = crossovers
        self.processors = processors
        self.selection = selection

        self.after_generation_callbacks = []

    def on_after_generation(self, callback: ICallback) -> None:
        self.after_generation_callbacks.append(callback)

    def run(self, population_size: int, gate_count: int, generations: int):
        population = self.seeder.seed(population_size, gate_count)

        for generation in range(1, generations):

            # TODO: Perform Elitism

            offspring = [circuit.copy() for circuit in population]

            # Shuffle to avoid crossover in the same proximity across
            # generations.
            random.shuffle(offspring)

            for crossover in self.crossovers:
                for circuit1, circuit2 in zip(offspring[:-1], offspring[1:]):
                    if random.random() < crossover.prob:
                        crossover.cross(circuit1, circuit2)

            for mutation in self.mutations:
                for circuit in offspring:
                    if random.random() < mutation.prob:
                        mutation.mutate(circuit)

            for processor in self.processors:
                processor.process(offspring)

            population = self.selection.select(offspring, population_size)

            for callback in self.after_generation_callbacks:
                callback(population)

        return population
