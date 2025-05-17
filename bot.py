from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Merhaba! Bot çalışıyor.")

app = ApplicationBuilder().token("7781380072:AAHH_4PWe1Nuau3j5fQ49ufLwDNalm66xS8
").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
