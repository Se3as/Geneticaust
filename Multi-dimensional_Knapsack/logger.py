import csv

class Log:

    def __init__(self, filename: str):
        self.filename = filename
        self.records = []
        self.header = ["problem", "time", "count", "sum"]

    def add(self, problem: str, time: float, count: int, sum: int):
        self.records.append({
            "problem": problem,
            "time": time,
            "count": count,
            "sum": sum
        })

    def save(self):
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.header)
                writer.writeheader()
                writer.writerows(self.records)
        except IOError as e:
            print(f"Error al escribir en el archivo '{self.filename}': {e}")