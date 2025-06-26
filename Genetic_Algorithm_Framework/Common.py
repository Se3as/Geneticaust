      
from typing import List

class GAConstants:
    RANDOM_INIT = 0
    HEURISTIC_INIT = 1
    
    ROULETTE_SELECTION = 0
    RANKING_SELECTION = 1
    TOURNAMENT_SELECTION = 2
    
    ONE_POINT_CROSSOVER = 0
    TWO_POINT_CROSSOVER = 1
    UNIFORM_CROSSOVER = 2
    
    BIT_FLIP_MUTATION = 0
    SWAP_MUTATION = 1


class Individual:
    def __init__(self, chromosome: List[int]):
        self.chromosome : List[int] = chromosome
        self.fitness: float = 0.0  
    def __eq__(self, other):
        return self.fitness == other.fitness and self.chromosome == other.chromosome
    def __lt__(self, other):
        return self.fitness < other.fitness


class GAParams:
    def __init__(self, pop_size: int = 100, init_method: int = GAConstants.RANDOM_INIT, selection_method: int = GAConstants.TOURNAMENT_SELECTION,
        tournament_size: int = 5, crossover_prob: float = 0.85, crossover_type: int = GAConstants.UNIFORM_CROSSOVER, mutation_prob: float = 0.05,
        gene_mutation_prob: float = 0.1, mutation_type: int = GAConstants.BIT_FLIP_MUTATION, elitism_fraction: float = 0.1, max_generations: int = 1000,
        patience: int = 50):
        self.pop_size = pop_size
        self.init_method = init_method
        self.selection_method = selection_method
        self.tournament_size = tournament_size
        self.crossover_prob = crossover_prob
        self.crossover_type = crossover_type
        self.mutation_prob = mutation_prob
        self.gene_mutation_prob = gene_mutation_prob
        self.mutation_type = mutation_type
        self.elitism_fraction = elitism_fraction
        self.max_generations = max_generations
        self.patience = patience
