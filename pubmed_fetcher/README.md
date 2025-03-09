# Research Paper Fetcher

This project fetches research papers from PubMed based on a user-specified query and filters out papers that do not have at least one author affiliated with a pharmaceutical or biotech company. The results are saved in a CSV file.

## Project Structure
```
research-paper-fetcher/
│-- pubmed_fetcher/
│   │-- __init__.py
│   │-- fetch.py        # Fetches research papers from PubMed API
│   │-- filter.py       # Filters out academic-only papers
│   │-- utils.py        # Utility functions for saving results
│-- cli.py              # Command-line interface for the program
│-- README.md           # Project documentation
│-- pyproject.toml      # Dependency management (Poetry)
│-- poetry.lock         # Lockfile for dependency versions
```

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/pubmed_ApiFetcher.git
cd pubmed_ApiFetcher
```

### 2. Install Dependencies
This project uses Poetry for dependency management. If you don’t have Poetry installed, install it first:
```sh
pip install poetry
```
Then install dependencies:
```sh
poetry install
```

## Usage
Run the program using the command:
```sh
poetry run python cli.py "your search query" -f results.csv
```

For debugging mode:
```sh
poetry run python cli.py "your search query" -f results.csv -d
```


## Tools and Libraries Used
- **Python 3.8+**: Core programming language.
- **Poetry**: Dependency management ([Poetry](https://python-poetry.org/)).
- **Requests**: To fetch research papers from PubMed API ([Requests](https://docs.python-requests.org/en/latest/)).

## Notes
- The filtering mechanism uses a list of company-related keywords to identify non-academic authors.
- If no relevant papers are found, the CSV file will not be created.

## License
This project is licensed under the MIT License.

