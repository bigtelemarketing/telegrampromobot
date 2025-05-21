
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "7996855061:AAFz6yh7CDhtRIRkhA0vSXjBJkcTIOBHXrE"

OFFERTE = {
    "WindTre": [
        "100 GIGA + minuti illimitati a 7,99€",
        "150 GIGA + minuti e SMS illimitati a 9,99€",
        "GIGA illimitati con fibra a casa a 19,90€"
    ],
    "TIM": [
        "80 GIGA + minuti illimitati a 8,99€",
        "200 GIGA + minuti e SMS illimitati a 12,99€"
    ],
    "Vodafone": [
        "100 GIGA + minuti illimitati a 9,99€",
        "150 GIGA + minuti, SMS e chiamate internazionali a 14,99€"
    ],
    "Fastweb": [
        "90 GIGA + minuti illimitati a 7,95€",
        "Fibra + Mobile a 19,95€"
    ],
    "Optima": [
        "80 GIGA + minuti a 5,95€",
        "150 GIGA + minuti + SMS a 8,95€"
    ],
    "Iliad": [
        "150 GIGA + minuti illimitati a 9,99€",
        "GIGA illimitati con fibra a 24,99€"
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton(operatore, callback_data=operatore)]
        for operatore in OFFERTE.keys()
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        "📱 Seleziona un operatore per vedere le offerte migliori e risparmiare:",
        reply_markup=reply_markup
    )

async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    operatore = query.data
    offerte = OFFERTE.get(operatore, [])
    testo = f"📢 Offerte attuali di {operatore}:

"
    for offerta in offerte:
        testo += f"🔹 {offerta}\n"
    await query.message.reply_text(testo)

if __name__ == "__main__":
    from telegram.ext import ApplicationBuilder

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_query))

    port = int(os.environ.get("PORT", 8443))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=f"https://telegrampromobot-02eo.onrender.com/"
    )
