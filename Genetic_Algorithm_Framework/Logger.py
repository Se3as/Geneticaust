import csv
from typing import Dict, Any, List 

from Common import GAConstants, get_init_method, get_selection, get_crossover, get_mutation

from GeneticAlgo import GeneticAlgorithm
class Logger:

    def __init__(self, filename: str):

        self.filename = filename
        self._results: List[Dict[str, Any]] = []

    def get_base_header(self) -> List[str]:
        return [
            "Rep_num", "Time", "Stop_Reason",
            "Generation", "Population", "Init_Method",
            "Selection_Method", "Tournament_Size", "Crossover_Rate",
            "Crossover_Type", "Mutation_Rate", "Mutation_Type",
            "elitism", "Max_Gen", "Patience"
        ]

    def get_data(self, ga: 'GeneticAlgorithm', repetition: int, time: float) -> Dict[str, Any]:
        params = ga.params
        tournament_size = ""
        if params.selection_method == GAConstants.TOURNAMENT_SELECTION:
            tournament_size = params.tournament_size

        base_data = {
            "Rep_num": repetition, 
            "Time": f"{time:.4f}",
            "Stop_Reason": ga.stop_reason, 
            "Generation": ga.generation,
            "Population": params.pop_size, 
            "Init_Method": get_init_method(params.init_method),
            "Selection_Method": get_selection(params.selection_method), 
            "Tournament_Size": tournament_size,
            "Crossover_Rate": params.crossover_prob, 
            "Crossover_Type": get_crossover(params.crossover_type),
            "Mutation_Rate": params.mutation_prob, 
            "Mutation_Type": get_mutation(params.mutation_type),
            "elitism": params.elitism, 
            "Max_Gen": params.max_generations,
            "Patience": params.patience
        }
        return base_data

    def log_result(self, ga: 'GeneticAlgorithm', repetition: int, time: float, extra_cols: Dict[str, Any] = None):

        data = self.get_data(ga, repetition, time)
        metrics = ga.problem.get_mets(ga.best.chromosome)
        data.update(metrics)
        if extra_cols:
            data.update(extra_cols)
        self._results.append(data)

    def close(self):
        base_header = self.get_base_header()
        base_header_set = set(base_header)
        all_keys = set()
        for result_dict in self._results:
            all_keys.update(result_dict.keys())
        extra_keys = all_keys - base_header_set
        sorted_extra_keys = sorted(list(extra_keys))
        final_header = base_header + sorted_extra_keys
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=final_header, restval="")
                writer.writeheader()
                writer.writerows(self._results)

        except IOError as e:
            print(f"Error al escribir en el archivo '{self.filename}': {e}")