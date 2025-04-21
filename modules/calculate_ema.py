def calculate_ema_signals(price_data, short_period=7, medium_period=14, long_period=28):
    closes = [candle["close"] for candle in price_data]

    def ema(data, period):
        k = 2 / (period + 1)
        ema_values = [sum(data[:period]) / period]
        for price in data[period:]:
            ema_values.append(price * k + ema_values[-1] * (1 - k))
        return ema_values

    short_ema = ema(closes, short_period)[-1]
    medium_ema = ema(closes, medium_period)[-1]
    long_ema = ema(closes, long_period)[-1]

    # Logic sinyal
    if short_ema > medium_ema > long_ema:
        signal = "BUY"
    elif short_ema < medium_ema < long_ema:
        signal = "SELL"
    else:
        signal = "NEUTRAL"

    return {
        "short_ema": round(short_ema, 2),
        "medium_ema": round(medium_ema, 2),
        "long_ema": round(long_ema, 2),
        "signal": signal
    }
