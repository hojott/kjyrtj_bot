import os
from datetime import date

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
    today = date.today()
    return (date(today.year, 11, 16) - today).days

if __name__ == "__main__":
    main()