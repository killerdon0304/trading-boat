from config import *
from chartink_api import fetch_chartink_data
from storage import load_data, save_data, process_stocks
from telegram_bot import send_stock_alerts

def main():
    api_data = fetch_chartink_data(SCAN_CLAUSE)
    old_data = load_data(DATA_FILE)

    updated_data, new_stocks = process_stocks(
        old_data,
        api_data,
        STOCK_EXPIRY_DAYS
    )

    if new_stocks:
        send_stock_alerts(
            TELEGRAM_BOT_TOKEN,
            TELEGRAM_CHAT_ID,
            new_stocks
        )

    save_data(DATA_FILE, updated_data)

    print("✅ Done")
    print("New stocks:", len(new_stocks))
    print("Total stored:", len(updated_data))

if __name__ == "__main__":
    main()
