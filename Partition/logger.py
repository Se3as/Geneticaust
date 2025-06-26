import csv

class Log:

    def __init__(self, filename: str):
        self.filename = filename
        self.records = []
        self.header = ["problem_name", "execution_time", "item_count", "item_sum"]

    def add(self, problem_name: str, execution_time: float, item_count: int, item_sum: int):
        self.records.append({
            "problem_name": problem_name,
            "execution_time": execution_time,
            "item_count": item_count,
            "item_sum": item_sum
        })

    def save(self):
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.header)
                writer.writeheader()
                writer.writerows(self.records)
        except IOError as e:
            print(f"Error al escribir en el archivo '{self.filename}': {e}")