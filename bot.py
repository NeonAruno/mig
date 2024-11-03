
TOKEN = "7163922987:AAHxvBbBUmW_z_Ircu0CHR1plEK7yGey1jo"


from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)
app = ApplicationBuilder().token(TOKEN).build()

@app.route('/webhook', methods=['POST'])
async def webhook() -> str:
    update = Update.de_json(request.get_json(force=True), app.bot)
    await app.process_update(update)
    return 'OK'

@app.route('/setwebhook', methods=['GET'])
def set_webhook():
    app.bot.set_webhook(url='https://app.koyeb.com/webhook')
    return 'Webhook set!'

if __name__ == '__main__':
    app.run(port=8443)
	
