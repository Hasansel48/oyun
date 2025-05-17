from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 👇 Buraya kendi bot token'ını doğrudan yazdım (senin verdiğin)
BOT_TOKEN = "7781380072:AAHH_4PWe1Nuau3j5fQ49ufLwDNalm66xS8"

# /start komutu çalıştığında çağrılır
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Oyunu Başlat", callback_game="NumberGo")]
    ])
    await update.message.reply_text(
        "🧩 NumberGo oyununa hoş geldin!\nAşağıdaki butona tıklayarak oyunu başlatabilirsin.",
        reply_markup=keyboard
    )

# Botu başlat
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
