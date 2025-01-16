#!/usr/bin/env python3

import numpy as np
from statistics import mean
from typing import List

from ga4qc.ga import GA
from ga4qc.seeder import RandomSeeder
from ga4qc.callback import ICallback
from ga4qc.processors import QuasimSimulator, JensenShannonFitness, NumericalOptimizer
from ga4qc.mutation import RandomGateMutation, ParameterChangeMutation
from ga4qc.crossover import OnePointCrossover
from ga4qc.selection import ISelection, TournamentSelection
from ga4qc.circuit import GateSet, Circuit
from ga4qc.circuit.gates import Identity, CX, S, T, H, RX


class PrintBestFitness(ICallback):
    def __call__(self, circuits: List[Circuit], generation: int) -> None:
        fitness_scores = [circuit.fitness_values[0] for circuit in circuits]

        mean_fitness = mean(fitness_scores)
        best_fitness = min(fitness_scores)
        best_idx = fitness_scores.index(best_fitness)

        print(f"\nBest fitness at gen {generation}: {best_fitness}")
        print(f"Mean fitness: {mean_fitness}")
        print(f"\t{circuits[best_idx]}")


if __name__ == "__main__":
    gate_set = GateSet([CX, RX, Identity], qubit_num=4)

    ga = GA(
        seeder=RandomSeeder(gate_set),
        mutations=[
            RandomGateMutation(gate_set, circ_prob=1, gate_prob=0.3),
            ParameterChangeMutation(0.1, 0.5),
        ],
        crossovers=[OnePointCrossover()],
        processors=[
            NumericalOptimizer(
                simulator=QuasimSimulator(),
                fitness=JensenShannonFitness(
                    target_dists=[
                        np.array([0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5])
                    ]
                ),
                rounds=10,
            ),
        ],
        selection=TournamentSelection(tourn_size=2),
    )

    ga.on_after_generation(PrintBestFitness())

    population = ga.run(population_size=50, gate_count=6, generations=20, elitism_count=5)
