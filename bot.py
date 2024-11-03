from flask import Flask
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

app = Flask(__name__)
TOKEN = "7163922987:AAHxvBbBUmW_z_Ircu0CHR1plEK7yGey1jo"

@app.route("/")
def health_check():
    return "Bot is running"
async def start(up: Update,con: CallbackContext) -> None:
	await up.message.reply_text("ok")
def run_server():
    app.run(host="0.0.0.0", port=8080)

def run_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_server).start()
    run_bot()
