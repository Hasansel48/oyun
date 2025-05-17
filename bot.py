from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7781380072:AAHH_4PWe1Nuau3j5fQ49ufLwDNalm66xS8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ /start komutu geldi!")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="🎮 NumberGo", callback_game={})]
    ])

    await update.message.reply_text(
        "🧩 NumberGo oyununa hoş geldin!\nAşağıdaki butona tıklayarak oyunu başlat.",
        reply_markup=keyboard
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
