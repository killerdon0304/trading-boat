import json
import os
from datetime import datetime, timedelta

DATE_FMT = "%Y-%m-%dT%H:%M:%S"

def load_data(filepath):
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON, resetting file")
        return []

def save_data(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def process_stocks(old_data, api_data, expiry_days):
    now = datetime.utcnow()

    old_map = {s["nsecode"]: s for s in old_data}
    api_map = {s["nsecode"]: s for s in api_data}

    updated = []
    new_stocks = []

    # ➕ Add / update stocks from API
    for code, stock in api_map.items():
        if code in old_map:
            stock["added_at"] = old_map[code]["added_at"]
        else:
            stock["added_at"] = now.strftime(DATE_FMT)
            new_stocks.append(stock)
        updated.append(stock)

    # ➖ Remove expired stocks
    for code, stock in old_map.items():
        if code not in api_map:
            try:
                added_at = datetime.strptime(stock["added_at"], DATE_FMT)
            except Exception:
                continue

            if now - added_at <= timedelta(days=expiry_days):
                updated.append(stock)

    return updated, new_stocks
