from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Doğrudan token (test için)
BOT_TOKEN = "7781380072:AAHH_4PWe1Nuau3j5fQ49ufLwDNalm66xS8"

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ /start komutu geldi!")  # Railway loglarında görünür

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="🎮 NumberGo", callback_game={})]  # oyun butonu
    ])

    await update.message.reply_text(
        "🎮 NumberGo oyununa hoş geldin!\nButona tıklayıp oyunu başlatabilirsin.",
        reply_markup=keyboard
    )

# /help komutu
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("ℹ️ /help komutu geldi!")
    await update.message.reply_text(
        "📋 Yardım:\n\n/start → Oyunu başlat\n/help → Yardım mesajı görüntüle"
    )

# Uygulamayı başlat
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.run_polling()
