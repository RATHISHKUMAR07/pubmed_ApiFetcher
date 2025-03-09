import csv
from typing import List, Dict

def save_to_csv(data: List[Dict], filename: str):
    """Saves filtered research papers to a CSV file."""
    if not data:
        print("No data available to save.")
        return

    keys = ["PMID", "Title", "PublicationDate", "NonAcademicAuthors", "CompanyAffiliations", "CorrespondingEmail"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"Data saved to {filename}")
