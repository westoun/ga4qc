#!/usr/bin/env python3

from ga4qc.ga import GA
from ga4qc.seeder import RandomSeeder
from ga4qc.callback import ICallback
from ga4qc.processors import IFitness, ISimulator
from ga4qc.mutation import RandomGateMutation
from ga4qc.crossover import OnePointCrossover
from ga4qc.selection import ISelection
from ga4qc.circuit import GateSet, Circuit

if __name__ == "__main__":
    gate_set = GateSet([], qubit_num=3)

    fitness = None
    simulator = None

    ga = GA(
        seeder=RandomSeeder(gate_set),
        mutations=[RandomGateMutation(gate_set, circ_prob=1, gate_prob=0.1)],
        crossovers=[OnePointCrossover()],
        processors=[simulator, fitness],
        selection=None,
    )

    ga.run(population_size=100, gate_count=20, generations=100)
