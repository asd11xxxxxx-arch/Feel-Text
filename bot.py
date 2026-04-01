import time
import os
from google import genai
import telebot

# --- Settings ---
# Render မှာ Environment Variables အနေနဲ့ ထည့်ရင် ပိုလုံခြုံပါတယ်
TELE_TOKEN = "8723958571:AAF7gnYStICGdm4fmO0k1Gkcj3kE44HIa8s"
GEMINI_KEY = "AIzaSyBVTOaJVYMLWN2wsjwHPJO8JRd44qZ58to"
CHANNEL_ID = "@feel_text_ch" 

client = genai.Client(api_key=GEMINI_KEY)
bot = telebot.TeleBot(TELE_TOKEN)

def get_ai_quote():
    prompt = "မြန်မာလို Feel စာသားတိုတိုလေး တစ်ကြောင်းရေးပေးပါ။ အလွမ်း၊ အဆွေး၊ အထီးကျန်တာ ဒါမှမဟုတ် ဘဝအကြောင်း ဖြစ်ရပါမယ်။ စာသားသက်သက်ပဲပေးပါ။"
    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text.strip()
    except:
        return None

if __name__ == "__main__":
    print("Bot is running on Render...")
    while True:
        content = get_ai_quote()
        if content:
            try:
                bot.send_message(CHANNEL_ID, content)
            except Exception as e:
                print(f"Error: {e}")
        
        # ၁ မိနစ် တစ်ခါ ပို့ဖို့ (၆၀ စက္ကန့်)
        time.sleep(60)
