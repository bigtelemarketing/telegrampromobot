
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "7996855061:AAFz6yh7CDhtRIRkhA0vSXjBJkcTIOBHXrE"

OFFERTE = {
    "WindTre": [
        "GIGA ILLIMITATI + minuti illimitati a 7,99€",
        "150 GIGA + minuti e SMS illimitati a 9,99€",
        "GIGA illimitati con fibra a casa a 19,90€"
    ],
    "TIM": [
        "100 GIGA + minuti illimitati a 5,99€",
        "150 GIGA + minuti e SMS illimitati a 6,99€"
    ],
    "Vodafone": [
        "100 GIGA + minuti illimitati a 9,99€",
        "150 GIGA + minuti, SMS e chiamate internazionali a 14,99€"
    ],
    "Fastweb": [
        "150 GIGA + minuti illimitati a 8,95€",
        "Fibra + Mobile a 23,95€"
    ],
    "Optima": [
        "100 GIGA + minuti illimitati a 4,95€",
        "250 GIGA 5G + minuti illimitati + SMS a 6,95€"
    ],"RICHIEDI SIM GRATIS"
    ],
    "Iliad": [
        "150 GIGA + minuti illimitati a 7,99€",
        "GIGA illimitati con fibra a 21,99€"
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton(operatore, callback_data=operatore)]
        for operatore in OFFERTE.keys()
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        "📱 Ciao sono il tuo consulente Seleziona un operatore per vedere le offerte migliori e risparmiare, scegli la promo e contattaci subito su www.bigtelemarketing.com OPPURE CONTATTACI NEL GRUPPO TELEGRAM https://t.me/+hYatPdFx44ZmNTQ8 ci sono tutti i contatti:",
        reply_markup=reply_markup
    )

async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    operatore = query.data
    offerte = OFFERTE.get(operatore, [])
    testo = f"📢 Offerte attuali di {operatore}:\n\n"

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
