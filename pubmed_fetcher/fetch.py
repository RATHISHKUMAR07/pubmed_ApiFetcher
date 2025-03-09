import re
import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def fetch_papers(query: str, max_results: int = 10) -> List[Dict]:
    """Fetch research papers from PubMed based on a query."""
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "xml"
    }

    search_response = requests.get(PUBMED_SEARCH_URL, params=search_params)
    search_tree = ET.fromstring(search_response.content)
    pmid_list = [pmid.text for pmid in search_tree.findall(".//Id")]

    if not pmid_list:
        return []

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pmid_list),
        "retmode": "xml"
    }

    fetch_response = requests.get(PUBMED_FETCH_URL, params=fetch_params)
    fetch_tree = ET.fromstring(fetch_response.content)
    
    papers = []
    for article in fetch_tree.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        pub_date = article.find(".//PubDate/Year")
        pub_date = pub_date.text if pub_date is not None else "Unknown"

        authors = []
        corresponding_email = "N/A"

        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            fore_name = author.find("ForeName")
            affiliation = author.find(".//Affiliation")
            
            name = f"{fore_name.text if fore_name is not None else ''} {last_name.text if last_name is not None else ''}".strip()
            affiliation_text = affiliation.text if affiliation is not None else ""

            # Extract email if found in affiliation text
            email_match = re.search(EMAIL_REGEX, affiliation_text)
            email = email_match.group(0) if email_match else None
            if email:
                corresponding_email = email  # Set the first found email

            authors.append({
                "name": name,
                "affiliation": affiliation_text,
                "email": email
            })

        papers.append({
            "PMID": pmid,
            "Title": title,
            "PublicationDate": pub_date,
            "Authors": authors,
            "CorrespondingEmail": corresponding_email  # Save first found email
        })

    return papers
