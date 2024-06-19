import csv

def read_csv(file_path: str) -> None:
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

# Example usage
read_csv('16u 2024 Midwestern Ontario Bearcats Summer 2024 Stats (1).csv')
