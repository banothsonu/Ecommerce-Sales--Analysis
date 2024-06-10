import requests

def get_ebay_items(app_id, query):
    url = "https://svcs.ebay.com/services/search/FindingService/v1"
    headers = {
        "X-EBAY-SOA-OPERATION-NAME": "findItemsByKeywords",
        "X-EBAY-SOA-SERVICE-VERSION": "1.0.0",
        "X-EBAY-SOA-REQUEST-DATA-FORMAT": "JSON",
        "X-EBAY-SOA-SECURITY-APPNAME": app_id,
    }
    params = {
        "keywords": query,
        "paginationInput.entriesPerPage": 10,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Example usage
app_id = 'YOUR_APP_ID'
query = 'laptop'
items = get_ebay_items(app_id, query)
print(items)