import os
from sec_api import ExtractorApi
from bs4 import BeautifulSoup


sec_token = "SEC-TOKEN"
extractor_api = ExtractorApi(sec_token)

def extract_section_from_10q(filing_name, filing_url):
    """
    Extracts Part 1, Item 1 section from a 10-Q filing and saves it to a text file.

    Args:
        filing_name (str): The name for the output text file.
        filing_url (str): The URL of the 10-Q filing.

    Returns:
        str: The name of the created text file.
    """
    try:
        # Extract the specified section from the 10-Q filing
        section_html = extractor_api.get_section(filing_url, section="part1item1", return_type='html')

        # Parse the HTML and extract text
        soup = BeautifulSoup(section_html, 'html.parser')
        section_text = soup.get_text()

        # Write the extracted text to a file
        text_file_name = f"data/10q/{filing_name}.txt"
        with open(text_file_name, "w") as textfile:
            textfile.write(section_text)

        return text_file_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    



def extract_section_from_10k(filing_name, filing_url):
    """
    Extracts Item 7 section from a 10-K filing and saves it to a text file.

    Args:
        filing_name (str): The name for the output text file.
        filing_url (str): The URL of the 10-K filing.

    Returns:
        str: The name of the created text file.
    """
    try:
        # Extract the specified section from the 10-K filing
        section_html = extractor_api.get_section(filing_url, section="7", return_type='html')

        # Parse the HTML and extract text
        soup = BeautifulSoup(section_html, 'html.parser')
        section_text = soup.get_text()

        # Write the extracted text to a file
        text_file_name = f"data/10k/{filing_name}.txt"
        with open(text_file_name, "w") as textfile:
            textfile.write(section_text)

        return text_file_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



"""
# example
filing_name = 'accenture'
filing_url = 'https://www.sec.gov/ix?doc=/Archives/edgar/data/1467373/000146737323000221/acn-20230531.htm'
extract_section_from_10q(filing_name, filing_url)
"""