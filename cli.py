import argparse
from pubmed_fetcher.fetch import fetch_papers
from pubmed_fetcher.filter import filter_non_academic_authors
from pubmed_fetcher.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed with filtering.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results as CSV", default="results.csv")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    papers = fetch_papers(args.query)

    if not papers:
        print("No papers found for the given query.")
        return

    print(f"Before filtering: Found {len(papers)} papers.")
    if args.debug and papers:
        print("Sample paper structure:", papers[0])

    filtered_papers = filter_non_academic_authors(papers)

    print(f"After filtering: {len(filtered_papers)} papers remain.")

    if not filtered_papers:
        print("No data to save.")
    else:
        save_to_csv(filtered_papers, args.file)
        print(f"Results saved to {args.file}")

if __name__ == "__main__":
    main()
