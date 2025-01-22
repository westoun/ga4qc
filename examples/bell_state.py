#!/usr/bin/env python3

import numpy as np
from statistics import mean
from typing import List

from ga4qc.ga import GA
from ga4qc.seeder import RandomSeeder
from ga4qc.callback import ICallback, FitnessStatsCallback, BestCircuitCallback
from ga4qc.processors import QuasimSimulator, JensenShannonFitness, NumericalOptimizer
from ga4qc.mutation import RandomGateMutation, ParameterChangeMutation
from ga4qc.crossover import OnePointCrossover
from ga4qc.selection import ISelection, TournamentSelection
from ga4qc.circuit import Circuit
from ga4qc.circuit.gates import Identity, CX, S, T, H, RX


class PrintFitnessStats(FitnessStatsCallback):
    def handle(
        self, fit_means, fit_mins, fit_maxs, fit_stdevs, generation=None
    ) -> None:
        print(f"\nFitness Stats at generation {generation}:")
        print(f"\tBest: {fit_mins[0]}")
        print(f"\tMean: {fit_means[0]}")
        print(f"\tstdev: {fit_stdevs[0]}")


class PrintBestCircuitStats(BestCircuitCallback):
    def handle(self, circuits: List[Circuit], generation=None):
        print(f"\nBest circuit at gen {generation}: {circuits[0]}")


def run():
    gate_set = [CX, RX, Identity]
    qubit_num = 4

    ga = GA(
        seeder=RandomSeeder(gate_set, qubit_num),
        mutations=[
            RandomGateMutation(gate_set, qubit_num, circ_prob=1, gate_prob=0.3),
            ParameterChangeMutation(circ_prob=1, gate_prob=0.3),
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

    ga.on_after_generation(PrintFitnessStats())
    ga.on_completion(PrintBestCircuitStats())

    ga.run(population_size=50, gate_count=6, generations=20, elitism_count=5)
