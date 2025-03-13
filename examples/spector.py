"""
Reimplements the genetic algorithm setup described in 
Spector, Lee, et al. "Quantum computing applications of genetic programming." 
Advances in genetic programming 3 (1999): 135-160. which builds
upon the fitness function presented in Spector, Lee, et al. "Genetic programming 
for quantum computers." Genetic Programming (1998): 365-373.
"""

import logging
import numpy as np
import random
from typing import List
from uuid import uuid4

from ga4qc.ga import GA
from ga4qc.seeder import RandomSeeder
from ga4qc.callback import ICallback, FitnessStatsCallback, BestCircuitCallback
from ga4qc.processors import QuasimSimulator, SpectorFitness
from ga4qc.mutation import RandomGateMutation
from ga4qc.crossover import OnePointCrossover
from ga4qc.selection import TournamentSelection
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
from ga4qc.params import GAParams


class LogFitnessStats(FitnessStatsCallback):
    def handle(
        self, fit_means, fit_mins, fit_maxs, fit_stdevs, generation=None
    ) -> None:
        logging.info(f"Best fitness at generation {generation}: {fit_mins[0]}")
        logging.info(
            f"Mean fitness at generation {generation}: {fit_means[0]}")


class LogBestCircuitStats(BestCircuitCallback):
    def handle(self, circuits: List[Circuit], generation=None):
        logging.info(f"Best circuit at generation {generation}: {circuits[0]}")


def run():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s",
        filename=f"experiment_spector_{str(uuid4())}.log",
        filemode="w",
    )

    # TODO: Replace halfadder task setup with actual target.

    HAOracle = OracleConstructor(
        sub_circuits=[
            [Identity()],  # case: input is 00
            [X(target=1)],  # case: input is 01
            [X(target=0)],  # case: input is 10
            [X(target=0), X(target=1)],  # case: input is 11
        ],
        name="Input",
    )

    target_dists: List[np.ndarray] = [
        np.kron([1, 0], [1, 0]),  # 00 => 00
        np.kron([1, 0], [0, 1]),  # 01 => 01
        np.kron([1, 0], [0, 1]),  # 10 => 01
        np.kron([0, 1], [1, 0]),  # 11 => 10
    ]

    ga_params = GAParams(
        population_size=200,
        chromosome_length=6,
        generations=50,
        elitism_count=5,
        qubit_num=3,
        ancillary_qubit_num=1,
        gate_set=[X, CX, CCX, Identity, HAOracle]
    )

    ga = GA(
        seeder=RandomSeeder(ga_params),
        mutations=[
            RandomGateMutation(ga_params,
                               circ_prob=0.4, gate_prob=0.2),
        ],
        crossovers=[OnePointCrossover(prob=0.4)],
        processors=[
            QuasimSimulator(),
            SpectorFitness(ga_params, target_dists=target_dists),
        ],
        selection=TournamentSelection(tourn_size=7),
    )

    ga.on_after_generation(LogFitnessStats())
    ga.on_after_generation(LogBestCircuitStats())

    ga.run(ga_params)


if __name__ == "__main__":
    random.seed(0)
    run()
