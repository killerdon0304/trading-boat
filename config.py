import os
# ===== Chartink =====
CHARTINK_HOME = "https://chartink.com"
CHARTINK_API = "https://chartink.com/screener/process"

SCAN_CLAUSE = """( {cash} ( ( {cash} ( ( {cash} (  weekly macd line( 21,3,9 ) >=  weekly macd signal( 21,3,9 ) and  weekly ha-close >  weekly "wma( ( ( 2 * wma( ( weekly ha-close), 15) ) - wma(( weekly ha-close), 30) ), 5)" and  1 week ago  ha-close <=  1 week ago  "wma( ( ( 2 * wma( ( weekly ha-close), 15) ) - wma(( weekly ha-close), 30) ), 5)" and  1 week ago ha-close <  weekly "wma( ( ( 2 * wma( ( 1 week ago min( 12 ,  weekly ha-close )), 15) ) - wma(( 1 week ago min( 12 ,  weekly ha-close )), 30) ), 5)" ) ) or( {cash} (  weekly ha-close >=  weekly "wma( ( ( 2 * wma( ( weekly ha-close), 22) ) - wma(( weekly ha-close), 44) ), 6)" and  1 week ago ha-close <  weekly "wma( ( ( 2 * wma( ( 1 week ago min( 12 ,  weekly ha-close )), 15) ) - wma(( 1 week ago min( 12 ,  weekly ha-close )), 30) ), 5)" and  weekly macd line( 11,3,9 ) >  weekly macd signal( 11,3,9 ) and  1 week ago  macd line( 11,3,9 ) <=  1 week ago  macd signal( 11,3,9 ) and  1 week ago max( 7 ,  1 week ago macd histogram( 21,3,9 ) ) <  0 ) ) ) ) and  weekly wma(  weekly rsi( 9 ) , 11 ) <  weekly rsi( 9 ) and  daily close >  50 and  1 day ago volume >  50000 and  market cap >  1000 and  weekly macd histogram( 21,3,9 ) >  0 and  weekly ha-close >  weekly ha-open and  daily close >  daily open and  weekly min( 10 ,  weekly macd histogram( 21,3,9 ) ) <  -20 and  weekly volume >  weekly sma(  weekly close , 7 ) ) )"""

# ===== Telegram =====
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# ===== Storage =====
DATA_FILE = "data/stocks.json"
STOCK_EXPIRY_DAYS = 7
