from typing import List, Tuple
import random
import itertools
from Common import GAParams, GAConstants  
from Problem import PartitionProblem, SubsetSumProblem, MultiDimensionalKnapsackProblem, BinPackingProblem
from Controller import Controller

def generate_case_bin_packing(n: int, max_size: int = 1000) -> Tuple[List[int], int]:
    item_sizes = [random.randint(1, max_size) for _ in range(n)]
    bin_capacity = max_size
    return item_sizes, bin_capacity

def generate_medium_case_numbers_partition(n: int, max_value: int = 1000) -> List[int]:
    medium_list: List[int] = [random.randint(1, max_value) for _ in range(n)]  
    if sum(medium_list) % 2 != 0:
        medium_list[-1] += 1
    return medium_list
def generate_case_mdkp(n: int, m: int = 3, max_value: int = 1000, max_weight: int = 1000) -> Tuple[List[int], List[List[int]], List[int]]:

    values = [random.randint(1, max_value) for _ in range(n)]
    weights = [[random.randint(1, max_weight) for _ in range(m)] for _ in range(n)]
    total_weights_per_dim = [sum(weights[i][j] for i in range(n)) for j in range(m)]
    capacities = [int(total_weight * 0.5) for total_weight in total_weights_per_dim]
    return values, weights, capacities

if __name__ == "__main__":
    random.seed(777)

    MDKP_OPTIMAL_VALUES = {
        50: 19957.0,
        100: 38194.0,
        200: 75679.0
    }

    sizes = [20]
    pop_sizes = [100, 200]
    selection_methods = [
        GAConstants.ROULETTE_SELECTION,
        GAConstants.TOURNAMENT_SELECTION,
        GAConstants.RANKING_SELECTION,
    ]
    crossover_probs = [0.8, 0.9]
    crossover_types = [
        GAConstants.ONE_POINT_CROSSOVER,
        GAConstants.UNIFORM_CROSSOVER,
        GAConstants.TWO_POINT_CROSSOVER
    ]
    mutation_types = [
        GAConstants.BIT_FLIP_MUTATION
    ]

    tournament_sizes = [2,5]
    mutation_probs = [0.01, 0.05]
    elitism_rates = [0.02]
    max_generations_list = [500]
    patiences = [50]

    controller = Controller(
        default_params=GAParams(),
        reps = 1
    )
    config_id = 1
    for size in sizes:
            numbers_p  = generate_medium_case_numbers_partition(size)
            numbers_s: List[int] = [random.randint(1, 1000) for _ in range(size)] 
            items_bp, capacity_bp = generate_case_bin_packing(size)
            values_mdkp, weights_mdkp, capacities_mdkp = generate_case_mdkp(size, m=3) 

            optimal_val_for_size = MDKP_OPTIMAL_VALUES.get(size)
            for (pop,
                selec,
                cross_prob,
                cross_type,
                mut_type,
                tour_size,
                mut_prob,
                elitism,
                max_gen,
                patience
                ) in itertools.product(
                    pop_sizes,
                    selection_methods,
                    crossover_probs,
                    crossover_types,
                    mutation_types,
                    tournament_sizes,
                    mutation_probs,
                    elitism_rates,
                    max_generations_list,
                    patiences
                ):

                ga_params = GAParams(
                    pop_size=pop,
                    init_method=GAConstants.RANDOM_INIT,
                    selection_method=selec,
                    tournament_size=tour_size,
                    crossover_prob=cross_prob,
                    crossover_type=cross_type,
                    mutation_prob=mut_prob,
                    mutation_type=mut_type,
                    elitism=elitism,
                    max_generations=max_gen,
                    patience=patience
                )

                problem_args = {'numbers': numbers_p}
                extra = {
                    'Size': size,
                    'Config_ID': config_id
                }
                controller.add_experiment(
                    problem=PartitionProblem,
                    problem_args=problem_args,
                    log_file=f"Partition_{size}.csv",
                    params=ga_params,
                    extra_info=extra
                )
                problem_args = {'numbers': numbers_s}
                controller.add_experiment(
                    problem=SubsetSumProblem,  
                    problem_args=problem_args,
                    log_file=f"SubsetSum_{size}.csv",
                    params=ga_params,
                    extra_info=extra
                )
                problem_args = {'values': values_mdkp,
                    'weights': weights_mdkp,
                    'capacities': capacities_mdkp, 
                    'optimal_value': optimal_val_for_size }
                controller.add_experiment(
                    problem = MultiDimensionalKnapsackProblem,
                    problem_args = problem_args,
                    log_file=f"MDKP_{size}.csv",
                    params=ga_params,
                    extra_info=extra
                )
                

                bp_ga_params = GAParams(
                    pop_size=pop, init_method=GAConstants.RANDOM_INIT,
                    selection_method=selec, tournament_size=tour_size,
                    crossover_prob=cross_prob, crossover_type=cross_type,
                    mutation_prob=mut_prob, 
                    mutation_type=GAConstants.SWAP_MUTATION, 
                    elitism=elitism, max_generations=max_gen, patience=patience)
                
                controller.add_experiment(
                    problem=BinPackingProblem,
                    problem_args={'item_sizes': items_bp, 'bin_capacity': capacity_bp},
                    log_file=f"BinPacking_{size}.csv",
                    params=bp_ga_params,
                    extra_info=extra
                )
                config_id += 1
    controller.run() 