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
from ga4qc.circuit.gates import (
    Identity,
    X,
    Y,
    Z,
    CX,
    S,
    T,
    H,
    RX,
    RY,
    RZ,
    CY,
    CZ,
    CCX,
    OracleConstructor,
    IGate,
)


class PrintFitnessStats(FitnessStatsCallback):
    def handle(self, fit_mean, fit_best, fit_worst, fit_stdev, generation=None) -> None:
        print(f"\nFitness Stats at generation {generation}:")
        print(f"\tBest: {fit_best}")
        print(f"\tMean: {fit_mean}")
        print(f"\tstdev: {fit_stdev}")


class PrintBestCircuitStats(BestCircuitCallback):
    def handle(self, circuit: Circuit, generation=None):
        print(f"\nBest circuit at gen {generation}: {circuit}")


def run():

    HAOracle = OracleConstructor(
        sub_circuits=[
            [Identity()],  # case: input is 00
            [X(target=1)],  # case: input is 01
            [X(target=0)],  # case: input is 10
            [X(target=0), X(target=1)],  # case: input is 11
        ],
        name="Input",
    )

    target_dists: List[List[float]] = [
        np.kron([1, 0], [1, 0]),  # 00 => 00
        np.kron([1, 0], [0, 1]),  # 01 => 01
        np.kron([1, 0], [0, 1]),  # 10 => 01
        np.kron([0, 1], [1, 0]),  # 11 => 10
    ]

    gate_set = [X, CX, CCX, Identity, HAOracle]

    ga = GA(
        seeder=RandomSeeder(gate_set, qubit_num=3),
        mutations=[
            RandomGateMutation(gate_set, qubit_num=3, circ_prob=1, gate_prob=0.3),
            # ParameterChangeMutation(circ_prob=0.1, gate_prob=0.1),
        ],
        crossovers=[OnePointCrossover()],
        processors=[
            QuasimSimulator(),
            JensenShannonFitness(target_dists=target_dists, ancillary_qubit_num=1),
        ],
        selection=TournamentSelection(tourn_size=2),
    )

    ga.on_after_generation(PrintFitnessStats())
    ga.on_completion(PrintBestCircuitStats())

    ga.run(
        population_size=200, gate_count=6, generations=50, elitism_count=5
    )
