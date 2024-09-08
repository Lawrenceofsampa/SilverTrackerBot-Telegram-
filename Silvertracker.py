import yfinance as yf
import telebot
import time


TELEGRAM_TOKEN = 'Token'
CHANNEL_ID = 'ChannelId' 

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Função para obter o preço atual da prata usando yfinance
def get_silver_price():
    silver_ticker = yf.Ticker("SI=F")
    silver_data = silver_ticker.history(period="1d")
    
    if not silver_data.empty:
        silver_price = silver_data['Close'].iloc[-1]
        return silver_price
    return None

# Função para enviar a atualização ao canal
def send_price_update(price, direction):
    direction_symbols = {
        "up": "🟩",
        "down": "🟥",
        "same": "⬜"
    }
    message = f"{direction_symbols[direction]} Silver is {price:.2f} USD per ounce"
    bot.send_message(CHANNEL_ID, message)

# Inicializa o último preço como None
last_price = None


while True:
    current_price = get_silver_price()
    
    if current_price is not None:
        if last_price is not None:
            if current_price > last_price:
                direction = "up"
            elif current_price < last_price:
                direction = "down"
            else:
                direction = "same"
        else:
            direction = "same"
        
        if last_price is None or current_price != last_price:
            send_price_update(current_price, direction)
            last_price = current_price  # Atualiza o último preço conhecido
            

    time.sleep(60)  # Verifica s
