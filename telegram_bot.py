import requests

STRATEGY_NAME = "Weekly Momentum – NH Mix Rules"

def send_single_stock(token, chat_id, stock):
    symbol = stock["nsecode"]

    # Links
    tv_weekly = f"https://www.tradingview.com/chart/?symbol=NSE:{symbol}&interval=W"
    dhan_trade = f"https://web.dhan.co/Charts?exch=BSE&seg=E&secid={stock["bsecode"]}"

    change = stock.get("per_chg", 0)
    emoji = "🟢" if change >= 0 else "🔴"

    msg = f"""
🏷️ <b>{STRATEGY_NAME}</b>

🚨 <b>New Stock Signal</b>

<b>{stock.get('name', '')}</b> <i>({symbol})</i>

━━━━━━━━━━━━━━
💰 <b>Price</b> : {stock.get('close')}
{emoji} <b>Change</b> : {change} %

📊 <b>Volume</b> : {stock.get('volume')}
━━━━━━━━━━━━━━

💬 <i>Tap a button below ⬇️</i>
""".strip()

    # 🔥 SIDE-BY-SIDE BUTTONS
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "📊 TradingView", "url": tv_weekly},
                {"text": "💹 Trade on Dhan", "url": dhan_trade}
            ]
        ]
    }

    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "HTML",
        "reply_markup": keyboard,
        "disable_web_page_preview": True
    }

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json=payload, timeout=10)


def send_stock_alerts(token, chat_id, stocks):
    for stock in stocks:
        send_single_stock(token, chat_id, stock)
