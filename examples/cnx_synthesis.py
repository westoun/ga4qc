#!/usr/bin/env python3

import numpy as np
import random
from statistics import mean
from typing import List

from ga4qc.ga import GA
from ga4qc.seeder import RandomSeeder
from ga4qc.callback import (
    ICallback,
    FitnessStatsCallback,
    BestCircuitCallback,
)
from ga4qc.processors import (
    QuasimSimulator,
    RemoveDuplicates,
    AbsoluteUnitaryDistance
)
from ga4qc.mutation import RandomGateMutation, ParameterChangeMutation
from ga4qc.crossover import OnePointCrossover
from ga4qc.selection import ISelection, TournamentSelection
from ga4qc.circuit import Circuit
from ga4qc.circuit.gates import Identity, CLIFFORD_PLUS_T
from ga4qc.params import GAParams


class PrintFitnessStats(FitnessStatsCallback):
    def handle(
        self, fit_means, fit_mins, fit_maxs, fit_stdevs, generation=None
    ) -> None:
        if generation % 5 == 0:
            print(f"\nFitness Stats at generation {generation}:")
            print(f"\tBest: {fit_mins[0]}")
            print(f"\tMean: {fit_means[0]}")
            print(f"\tstdev: {fit_stdevs[0]}")


class PrintBestCircuitStats(BestCircuitCallback):
    def handle(self, circuits: List[Circuit], generation=None):
        print(f"\nBest circuit at gen {generation}: {circuits[0]}")


def create_cnx_unitary(qubit_num: int) -> np.ndarray:
    dim = 2 ** qubit_num

    unitary = np.zeros((dim, dim), dtype=np.complex128)

    for i in range(dim):
        if i == dim - 1:
            unitary[i, i - 1] = 1
        elif i == dim - 2:
            unitary[i, i + 1] = 1
        else:
            unitary[i, i] = 1

    return unitary


def run():
    qubit_num = 2

    ga_params = GAParams(
        population_size=50,
        chromosome_length=20,
        generations=100,
        elitism_count=5,
        qubit_num=qubit_num,
        gate_set=CLIFFORD_PLUS_T + [Identity]
    )

    target_unitary = create_cnx_unitary(qubit_num)

    seeder = RandomSeeder(ga_params)

    ga = GA(
        seeder=seeder,
        mutations=[
            RandomGateMutation(ga_params, circ_prob=1, gate_prob=0.3),
        ],
        crossovers=[OnePointCrossover()],
        processors=[
            RemoveDuplicates(seeder=seeder),
            QuasimSimulator(),
            AbsoluteUnitaryDistance(
                ga_params, target_unitaries=[target_unitary])
        ],
        selection=TournamentSelection(tourn_size=2),
    )

    ga.on_after_generation(PrintFitnessStats())
    ga.on_completion(PrintBestCircuitStats())

    ga.run(ga_params)


if __name__ == "__main__":
    random.seed(0)
    run()
