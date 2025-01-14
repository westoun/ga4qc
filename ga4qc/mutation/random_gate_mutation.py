import random

from .interface import IMutation
from ga4qc.circuit import Circuit, GateSet


class RandomGateMutation(IMutation):

    prob: float
    gate_set: GateSet

    def __init__(self, gate_set: GateSet, prob: float):
        self.gate_set = gate_set
        self.prob = prob

    def mutate(self, circuit: Circuit) -> None:
        for i, gate in enumerate(circuit.gates):
            if random.random() < self.prob:
                circuit.gates[i] = self.gate_set.random_gate()
