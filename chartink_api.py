import requests
from urllib.parse import unquote
from config import SCAN_CLAUSE

def fetch_chartink_data(scan_clause):
    session = requests.Session()
    session.get("https://chartink.com")

    xsrf = unquote(session.cookies.get("XSRF-TOKEN"))

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-XSRF-TOKEN": xsrf
    }

    payload = {"scan_clause": scan_clause}

    res = session.post(
        "https://chartink.com/screener/process",
        json=payload,
        headers=headers,
        timeout=15
    )

    res.raise_for_status()
    return res.json()["data"]


if __name__ == "__main__":
    print(fetch_chartink_data(SCAN_CLAUSE))