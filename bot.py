from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Railway'de tanımlanacak

# /start komutu → kullanıcıya oyun butonu gönder
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Oyunu Başlat", callback_game="NumberGo")]  # işte burası!
    ])
    await update.message.reply_text(
        "🧩 10x10 NumberGo oyununa hoş geldin!\nButona tıklayarak oyunu başlat.",
        reply_markup=keyboard
    )

# Bot uygulamasını başlat
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
