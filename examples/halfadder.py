#!/usr/bin/env python3

import numpy as np
from statistics import mean
from typing import List

from ga4qc.ga import GA
from ga4qc.seeder import RandomSeeder
from ga4qc.callback import ICallback, FitnessStatsCallback, BestCircuitCallback
from ga4qc.processors import QuasimSimulator, JensenShannonFitness, GateCountFitness
from ga4qc.mutation import RandomGateMutation, ParameterChangeMutation
from ga4qc.crossover import OnePointCrossover
from ga4qc.selection import ISelection, TournamentSelection, NSGA2
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
    def handle(
        self, fit_means, fit_mins, fit_maxs, fit_stdevs, generation=None
    ) -> None:
        print(f"\nFitness Stats at generation {generation}:")
        print(f"\tBest: {fit_mins}")
        print(f"\tMean: {fit_means}")
        print(f"\tstdev: {fit_stdevs}")


class PrintBestCircuitStats(BestCircuitCallback):
    def handle(self, circuits: List[Circuit], generation=None):
        print(f"\nBest circuit at gen {generation}:")
        for obj_i, circuit in enumerate(circuits):
            print(f"Objective {obj_i}: {circuit}")


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

    gate_count = 6
    qubit_num = 3

    ga = GA(
        seeder=RandomSeeder(gate_set, gate_count=gate_count, qubit_num=qubit_num),
        mutations=[
            RandomGateMutation(gate_set, qubit_num=3, circ_prob=1, gate_prob=0.3),
            # ParameterChangeMutation(circ_prob=0.1, gate_prob=0.1),
        ],
        crossovers=[OnePointCrossover()],
        processors=[
            QuasimSimulator(),
            JensenShannonFitness(target_dists=target_dists, ancillary_qubit_num=1),
            GateCountFitness(),
        ],
        selection=NSGA2(),
    )

    ga.on_after_generation(PrintFitnessStats(objective_count=2))
    ga.on_completion(PrintBestCircuitStats(objective_count=2))

    ga.run(population_size=200, gate_count=gate_count, generations=50, elitism_count=5)
