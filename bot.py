from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Doğrudan token (test için)
BOT_TOKEN = "7781380072:AAHH_4PWe1Nuau3j5fQ49ufLwDNalm66xS8"

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ /start komutu geldi!")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="🎮 NumberGo", callback_game={})]
    ])
    await update.message.reply_text(
        "🎮 NumberGo oyununa hoş geldin!\nAşağıdaki butona tıklayarak oyunu başlatabilirsin.",
        reply_markup=keyboard
    )

# /help komutu
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("ℹ️ /help komutu geldi!")
    await update.message.reply_text("📋 Yardım:\n/start → Oyunu başlat\n/help → Yardım mesajı")

# Her mesajı logla (test için)
async def echo_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"🟡 Kullanıcıdan mesaj geldi: {update.message.text}")

# Botu başlat
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.ALL, echo_all))  # gelen tüm mesajları logla
app.run_polling()
