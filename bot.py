import time
from google import genai
import telebot
from flask import Flask
from threading import Thread

# --- Flask Server for Render Port Check ---
app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# --- Bot Settings ---
TELE_TOKEN = "8723958571:AAF7gnYStICGdm4fmO0k1Gkcj3kE44HIa8s"
GEMINI_KEY = "AIzaSyBVTOaJVYMLWN2wsjwHPJO8JRd44qZ58to"
CHANNEL_ID = "@feel_text_ch"

client = genai.Client(api_key=GEMINI_KEY)
bot = telebot.TeleBot(TELE_TOKEN)

def start_posting():
    print("AI Posting started...")
    while True:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents="မြန်မာလို Feel စာသားတိုတိုလေး တစ်ကြောင်းရေးပေးပါ။ အလွမ်း၊ အဆွေး၊ အထီးကျန်တာ ဒါမှမဟုတ် ဘဝအကြောင်း ဖြစ်ရပါမယ်။ စာသားသက်သက်ပဲပေးပါ။"
            )
            content = response.text.strip()
            if content:
                bot.send_message(CHANNEL_ID, content)
                print(f"Posted: {content}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60) # ၁ မိနစ် တစ်ခါ

if __name__ == "__main__":
    # Flask ကို Background မှာ Run မယ် (Render Error မတက်အောင်)
    t = Thread(target=run_flask)
    t.start()
    # Bot ကို စတင်မယ်
    start_posting()

