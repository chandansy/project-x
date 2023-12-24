import requests
from bs4 import BeautifulSoup



def get_company_info(company_url: str):
    """
    Scrape company details from the company's website
    """


    # if there is not a http in the url, add it
    if not company_url.startswith("http"):
        company_url = "http://" + company_url

    try:    
        response_data = requests.get(company_url)
        print(response_data.status_code)
    except Exception as e:
        print("Exception occurred while fetching company details", e)
        return None

    soup = BeautifulSoup(response_data.text, 'html.parser')
    company_dump = soup.get_text()

    # remove all the new lines
    company_dump = company_dump.replace("\n", " ")
    # remove all the tabs
    company_dump = company_dump.replace("\t", " ")
    # remove all the double spaces
    company_dump = company_dump.replace("  ", " ")

    return company_dump




