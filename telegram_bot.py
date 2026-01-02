import requests

STRATEGY_NAME = "Weekly Momentum – NH Mix Rules"

def send_single_stock(token, chat_id, stock):
    # Weekly chart link (TradingView)
    tv_link = (
        f"https://www.tradingview.com/chart/"
        f"?symbol=NSE:{stock['nsecode']}&interval=W"
    )

    change = stock.get("per_chg", 0)
    change_emoji = "🟢" if change >= 0 else "🔴"

    msg = f"""
    🏷️ <b>{STRATEGY_NAME}</b>
    
    🚨 <b>New Stock Signal</b>

<b>{stock.get('name', '')}</b> <i>- {stock['nsecode']}</i>

━━━━━━━━━━━━━━
💰 <b>Price</b> : {stock.get('close')}
{change_emoji} <b>Change</b> : {change} %

📊 <b>Volume</b> : {stock.get('volume')}
━━━━━━━━━━━━━━

📈 <a href="{tv_link}">Open Weekly Chart (TradingView)</a>
💬 <i>Discuss below ⬇️</i>
"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg.strip(),
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    requests.post(url, json=payload, timeout=10)


def send_stock_alerts(token, chat_id, stocks):
    for stock in stocks:
        send_single_stock(token, chat_id, stock)
