from dataclasses import dataclass


@dataclass
class GAParams:
    population_size: int
    chromosome_length: int
    generations: int
    qubit_num: int 
    ancillary_qubit_num: int = 0
    elitism_count: int = 0
