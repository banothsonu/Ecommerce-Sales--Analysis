import requests

# Get the webpage
url = "https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data"
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
  content = response.text

  # Search for the download link (heuristic approach, may need adjustment)
  download_link_start = content.find('href="/datasets/')
  if download_link_start != -1:
    # Extract the link text
    start_index = download_link_start + 6  # Move past "href=\""
    end_index = content.find('"', start_index)
    download_link = content[start_index:end_index]
    print("Download link:", download_link)
  else:
    print("Download link not found. Please check the website for download instructions.")
else:
  print("Error: Failed to get webpage. Status code:", response.status_code)
