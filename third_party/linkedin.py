import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    # api_key = 'MRnBB1L_TfNoJHogPn3xQw'
    # headers = {'Authorization': 'Bearer ' + api_key}
    # api_endpoint = 'https://gist.githubusercontent.com/sonagihu/ab71ee6aee732110289da42be8331334/raw/69f06cfcfa75d8bc9593db06c47ddd3cb9a77f45/gistfile1.txt'

    response = requests.get(linkedin_profile_url)

    data = response.json()

    #  minimize token for LLM
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
