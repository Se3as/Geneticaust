from typing import List
from Common import GAParams, GAConstants  
from GeneticAlgo import GeneticAlgorithm
from Problem import PartitionProblem  


if __name__ == "__main__":

    numbers: List[int] = [24, 40, 22, 42, 7, 4, 2, 9] 

    partition_problem = PartitionProblem(numbers)

    ga_params = GAParams(
    pop_size=500,                  
    init_method=GAConstants.RANDOM_INIT,
    selection_method=GAConstants.TOURNAMENT_SELECTION,
    tournament_size=5,
    crossover_prob=0.9,
    crossover_type=GAConstants.UNIFORM_CROSSOVER,
    mutation_prob=0.25,                
    gene_mutation_prob=0.1,            
    mutation_type=GAConstants.BIT_FLIP_MUTATION,
    elitism=0.05,             
    max_generations=500,             
    patience=50                      
    )
    genetic_algorithm = GeneticAlgorithm(partition_problem, ga_params)
    best_solution = genetic_algorithm.run()
    print("\nTermino en " + str(genetic_algorithm.generation) + " generaciones.")
    print("Fitness : " + str(round(best_solution.fitness, 2)))

