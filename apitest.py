import requests
# import pandas as pd
from urllib.parse import unquote

URL = "https://chartink.com/screener/process"

session = requests.Session()

# STEP 1: GET homepage to set cookies
home = session.get("https://chartink.com")

# STEP 2: Extract XSRF token from cookies
xsrf_token = session.cookies.get("XSRF-TOKEN")
xsrf_token = unquote(xsrf_token)  # VERY IMPORTANT

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "X-XSRF-TOKEN": xsrf_token,
    "Referer": "https://chartink.com/screener/nh-mix-rules-30-hma-2987"
}

SCAN_CLAUSE = """( {cash} ( ( {cash} ( ( {cash} (  weekly macd line( 21,3,9 ) >=  weekly macd signal( 21,3,9 ) and  weekly ha-close >  weekly "wma( ( ( 2 * wma( ( weekly ha-close), 15) ) - wma(( weekly ha-close), 30) ), 5)" and  1 week ago  ha-close <=  1 week ago  "wma( ( ( 2 * wma( ( weekly ha-close), 15) ) - wma(( weekly ha-close), 30) ), 5)" and  1 week ago ha-close <  weekly "wma( ( ( 2 * wma( ( 1 week ago min( 12 ,  weekly ha-close )), 15) ) - wma(( 1 week ago min( 12 ,  weekly ha-close )), 30) ), 5)" ) ) or( {cash} (  weekly ha-close >=  weekly "wma( ( ( 2 * wma( ( weekly ha-close), 22) ) - wma(( weekly ha-close), 44) ), 6)" and  1 week ago ha-close <  weekly "wma( ( ( 2 * wma( ( 1 week ago min( 12 ,  weekly ha-close )), 15) ) - wma(( 1 week ago min( 12 ,  weekly ha-close )), 30) ), 5)" and  weekly macd line( 11,3,9 ) >  weekly macd signal( 11,3,9 ) and  1 week ago  macd line( 11,3,9 ) <=  1 week ago  macd signal( 11,3,9 ) and  1 week ago max( 7 ,  1 week ago macd histogram( 21,3,9 ) ) <  0 ) ) ) ) and  weekly wma(  weekly rsi( 9 ) , 11 ) <  weekly rsi( 9 ) and  daily close >  50 and  1 day ago volume >  50000 and  market cap >  1000 and  weekly macd histogram( 21,3,9 ) >  0 and  weekly ha-close >  weekly ha-open and  daily close >  daily open and  weekly min( 10 ,  weekly macd histogram( 21,3,9 ) ) <  -20 and  weekly volume >  weekly sma(  weekly close , 7 ) ) )"""

payload = {
    "scan_clause": SCAN_CLAUSE
}

# STEP 3: POST request
response = session.post(URL, json=payload, headers=HEADERS)
response.raise_for_status()

data = response.json()["data"]

# df = pd.DataFrame(data)
# df.to_csv("NH_Mix_Rules_30_HMA.csv", index=False)

print("✅ SUCCESS")
# print("Stocks found:", len(df))
# print(df[["nsecode", "name", "close"]].head())
print(data)
