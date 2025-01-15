import random
from typing import List

from ga4qc.mutation import IMutation
from ga4qc.crossover import ICrossover
from ga4qc.simulator import ISimulator
from ga4qc.circuit import Circuit, GateSet
from ga4qc.fitness import IFitness
from ga4qc.circuit_processor import ICircuitProcessor
from ga4qc.selection import ISelection
from ga4qc.seeder import ISeeder
from ga4qc.stop_condition import IStopCondition


class GA:

    seeder: ISeeder
    mutations: List[IMutation]
    crossovers: List[ICrossover]
    circuit_processors: List[ICircuitProcessor]
    selection: ISelection
    stop_conditions: List[IStopCondition]

    def __init__(
        self,
        seeder: ISeeder,
        mutations: List[IMutation],
        crossovers: List[ICrossover],
        circuit_processors: List[ICircuitProcessor],
        selection: ISelection,
        stop_conditions: List[IStopCondition],
    ):
        # TODO: Add default values for unspecified
        # operators.
        self.seeder = seeder
        self.mutations = mutations
        self.crossovers = crossovers
        self.circuit_processors = circuit_processors
        self.selection = selection
        self.stop_conditions = stop_conditions

    def run(self, population_size: int, gate_count: int, generations: int):
        population = self.seeder.seed(population_size, gate_count)

        for generation in range(1, generations):

            # TODO: Perform Elitism

            # TODO: Clone Population

            random.shuffle(population)

            for crossover in self.crossovers:
                for circuit1, circuit2 in zip(population[:-1], population[1:]):
                    if random.random() < crossover.prob:
                        crossover.cross(circuit1, circuit2)

            for mutation in self.mutations:
                for circuit in population:
                    if random.random() < mutation.prob:
                        mutation.mutate(circuit)

            for circuit_processor in self.circuit_processors:
                circuit_processor.process(population)

            population = self.selection.select(population)

            stop = False
            for stop_condition in self.stop_conditions:
                if stop_condition.is_met(population):
                    stop = True
                    break

            if stop:
                break
