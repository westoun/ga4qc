from dataclasses import dataclass


@dataclass
class GAParams:
    population_size: int
    chromosome_length: int
    generations: int
    elitism_count: int = 0
