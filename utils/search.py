import requests
from config.config import GOOGLE_API_KEY, GOOGLE_CSE_ID

def web_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
    }
    response = requests.get(url, params=params)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())  # Add this line to inspect the result
    if response.status_code == 200:
        results = response.json().get("items", [])
        return [item["snippet"] for item in results[:3]]
    else:
        return ["No results found."]
