#!/usr/bin/env python3

from ga4qc.ga import GA
from ga4qc.seeder import RandomSeeder
from ga4qc.callback import ICallback
from ga4qc.processors import IFitness, ISimulator, QuasimSimulator
from ga4qc.mutation import RandomGateMutation
from ga4qc.crossover import OnePointCrossover
from ga4qc.selection import ISelection, TournamentSelection
from ga4qc.circuit import GateSet, Circuit
from ga4qc.circuit.gates import Identity, CX, S, T, H

if __name__ == "__main__":
    gate_set = GateSet([Identity, CX, S, T, H], qubit_num=3)

    fitness = None

    ga = GA(
        seeder=RandomSeeder(gate_set),
        mutations=[RandomGateMutation(gate_set, circ_prob=1, gate_prob=0.1)],
        crossovers=[OnePointCrossover()],
        processors=[QuasimSimulator(), fitness],
        selection=TournamentSelection(tourn_size=2),
    )

    ga.run(population_size=100, gate_count=20, generations=100)
