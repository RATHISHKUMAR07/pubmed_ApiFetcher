from typing import List, Dict

COMPANY_KEYWORDS = [
    "pharma", "biotech", "inc", "ltd", "corporation", "gmbh", "s.a.", "corp",
    "biosciences", "laboratories", "therapeutics", "genomics", "medical",
    "diagnostics", "solutions", "technologies", "lifesciences", "clinic",
    "hospital", "oncology", "research institute", "medtech", "consulting", "center"
]

UNIVERSITY_KEYWORDS = [
    "university", "institute", "school", "college", "academy", "research center"
]

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """Filters out papers with only academic authors and extracts required details."""
    
    filtered_papers = []

    for paper in papers:
        academic_authors = []
        non_academic_authors = []
        company_affiliations = set()
        corresponding_email = paper.get("CorrespondingEmail", "N/A")  # Use extracted email

        for author in paper.get("Authors", []):
            affiliation = author.get("affiliation", "").lower().strip()
            author_name = author.get("name", "Unknown")

            if any(keyword in affiliation for keyword in COMPANY_KEYWORDS):
                non_academic_authors.append(author_name)
                company_affiliations.add(affiliation)

            elif any(keyword in affiliation for keyword in UNIVERSITY_KEYWORDS):
                academic_authors.append(author)

        if non_academic_authors:  # Keep only papers with at least one non-academic author
            filtered_papers.append({
                "PMID": paper.get("PMID", "N/A"),
                "Title": paper.get("Title", "No Title"),
                "PublicationDate": paper.get("PublicationDate", "N/A"),
                "NonAcademicAuthors": non_academic_authors if non_academic_authors else ["N/A"],
                "CompanyAffiliations": list(company_affiliations) if company_affiliations else ["N/A"],
                "CorrespondingEmail": corresponding_email,
            })

    return filtered_papers
