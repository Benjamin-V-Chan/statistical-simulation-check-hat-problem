import csv

def save_to_csv(data: list, file_path: str):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        for item in data:
            writer.writerow([item])

def load_from_csv(file_path: str) -> list:
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        return [int(row[0]) for row in reader]