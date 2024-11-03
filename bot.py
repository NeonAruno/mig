from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler,CallbackContext,ApplicationBuilder,MessageHandler,filters

TOKEN = "7163922987:AAHxvBbBUmW_z_Ircu0CHR1plEK7yGey1jo"

chats = [-1001922791146]
async def start(up: Update,con: CallbackContext)-> None:
	message = up.message
	await message.reply_text("ok")


async def handlerf(up: Update,con: CallbackContext)-> None:
	message = up.channel_post
	print(message.chat)
	try:
		if(message.photo and message.chat.id in chats):
			photo = message.photo[-1].file_id
			caption = f"<b>{message.caption}\n\n<i>#new_post</i></b>"
			key = [
					[InlineKeyboardButton("🍿 REGARDER 🍿",url=f"t.me/{message.chat.username}/{message.id}")],
					[InlineKeyboardButton("⭐ Plus d'animer ⭐",url="https://t.me/+QtT1awr74l5iYWQ0")]
				]
			reply_markup = InlineKeyboardMarkup(key)
			if "https://" not in caption:
				await con.bot.send_photo(chat_id=-1001928904816,photo=photo,caption=caption,reply_markup=reply_markup,parse_mode="HTML")
			#for chat in chats:
			#	await con.bot.delete_message(chat_id=chat,message_id,=message.id)
			#	
	except Exception as e:
		print(e)


def main():
	app = ApplicationBuilder().token(TOKEN).build()
	app.add_handler(CommandHandler("start",start))
	app.add_handler(MessageHandler(filters.ChatType.CHANNEL,handlerf))
	print("Bot en marche")
	app.run_polling()
	

if __name__ == "__main__":
	main()
