def format_signal(coin, price_data, ema_signal, rsi, volume, whale_alerts):
    whale_info = "\n".join([str(w) for w in whale_alerts]) if whale_alerts else "No recent whale activity"

    return f"""
    Coin: {coin.upper()}
    Price (USD): {price_data.get("price_usd", "N/A")}
    EMA Signal: {ema_signal}
    RSI: {round(rsi, 2) if isinstance(rsi, (int, float)) else rsi}
    24h Volume: {volume.get("24h_volume", "N/A")}
    Whale Alerts:
    {whale_info}
    """.strip()
