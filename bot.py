import os
from zoneinfo import ZoneInfo
from datetime import date, datetime

import dotenv
from telebot import TeleBot

def main():
    dotenv.load_dotenv()
    _token = os.environ.get("TELEGRAM_BOT_TOKEN")
    kjyrtj = TeleBot(_token)


    @kjyrtj.message_handler(func=lambda msg: True)
    def send_tj(message):
        kjyrtj.reply_to(message, f"KJYR tj: {tj()} pv")

    kjyrtj.infinity_polling()


def tj() -> int:
    # TODO: automate getting date from calendar
    tz = ZoneInfo("Europe/Helsinki")
    t = date.today()
    today = datetime(t.year, t.month, t.day).astimezone(tz)
    kjyr  = datetime(t.year, 11, 16).astimezone(tz)
    return (kjyr - today).days

if __name__ == "__main__":
    main()
