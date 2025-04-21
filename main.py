from modules.fetch_price import fetch_price_data
from modules.fetch_volume import fetch_volume_data
from modules.calculate_ema import calculate_ema_signals
from modules.calculate_rsi import calculate_rsi
from modules.sheet_logger import log_to_sheet
from modules.whale_alert import fetch_whale_data
from utils.signal_formatter import format_signal
from utils.telegram_notifier import send_telegram_message
import time

COINS = ["bitcoin", "ethereum", "solana", "ripple", "dogecoin"]

while True:
    for coin in COINS:
        try:
            price_data = fetch_price_data(coin)
            volume_data = fetch_volume_data(coin)
            ema_signal = calculate_ema_signals(price_data)
            rsi_value = calculate_rsi(price_data)
            whale_alerts = fetch_whale_data(coin)

            signal = format_signal(
                coin=coin,
                price_data=price_data,
                ema_signal=ema_signal,
                rsi=rsi_value,
                volume=volume_data,
                whale_alerts=whale_alerts
            )

            log_to_sheet(signal)
            send_telegram_message(signal)
            print(signal)

        except Exception as e:
            print(f"{coin.upper()} error: {e}")

    time.sleep(300)  # 5 menit
