import requests

url = "https://fbref.com/en/comps/1/World-Cup-Stats"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers, timeout=20)

print("Status code:", response.status_code)

if response.status_code == 200:
    print("Ket noi FBref thanh cong!")
else:
    print("Khong ket noi duoc FBref.")