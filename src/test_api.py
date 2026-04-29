import requests
import json

url = "https://www.nemoapp.kr/api/store/search-list?Subway=222&Radius=1000&CompletedOnly=false&NELat=37.51140055648316&NELng=127.03456544361883&SWLat=37.498879807111344&SWLng=127.02080817937446&Zoom=15&SortBy=29&PageIndex=0"
headers = {
    "referer": "https://www.nemoapp.kr/store",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
data = response.json()

if "items" in data and len(data["items"]) > 0:
    print(json.dumps(data["items"][0], indent=4, ensure_ascii=False))
else:
    print("No items found or unexpected response structure.")
    print(data)
