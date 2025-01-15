from functools import partial
import numpy as np
from scipy.optimize import minimize, OptimizeResult
from typing import List, Tuple, Union

from ga4qc.circuit import Circuit
from ga4qc.circuit.gates import IOptimizableGate
from .interface import ICircuitProcessor
from .fitness import IFitness
from .simulator import ISimulator


def extract_params(circuit: Circuit) -> List[float]:
    params = []
    for gate in circuit.gates:
        if issubclass(gate, IOptimizableGate):
            params.extend(gate.params)

    return params


def get_bounds(params: List[float]) -> List[Tuple[float, float]]:
    bounds = []
    for _ in params:
        bounds.append((-np.pi, np.pi))
    return bounds


def update_circuit(circuit: Circuit, params: List[float]) -> None:
    for gate in circuit.gates:
        if issubclass(gate, IOptimizableGate):
            param_count = len(gate.params)

            gate_params, params = (params[:param_count], params[param_count:])
            gate.set_params(gate_params)


def evaluate(
    params: List[float], circuit: Circuit, simulator: ISimulator, fitness: IFitness
) -> float:
    update_circuit(circuit, params)
    simulator.process([circuit])
    fitness.process([circuit])
    score = circuit.fitness_values[0]
    return score


class NumericalOptimizer(ICircuitProcessor):
    simulator: ISimulator
    fitness: IFitness
    rounds: int

    def __init__(self, simulator: ISimulator, fitness: IFitness, rounds: int = 10):
        self.simulator = simulator
        self.fitness = fitness
        self.rounds = rounds

    def process(self, circuits: List[Circuit]) -> None:
        for circuit in circuits:
            initial_params = extract_params(circuit)

            if len(initial_params) == 0:
                self.simulator.process([circuit])
                self.fitness.process([circuit])
                continue

            bounds = get_bounds(circuit)

            objective_function = partial(
                evaluate,
                circuit=circuit,
                simulator=self.simulator,
                fitness=self.fitness,
            )

            optimization_result: OptimizeResult = minimize(
                objective_function,
                x0=initial_params,
                method="Nelder-Mead",
                bounds=bounds,
                tol=self.params.tolerance,
                options={"maxiter": self.rounds, "disp": False},
            )

            best_params = optimization_result.x
            update_circuit(circuit, best_params)
