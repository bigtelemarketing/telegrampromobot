import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Inserisci direttamente il tuo token
TOKEN = "7996855061:AAFz6yh7CDhtRIRkhA0vSXjBJkcTIOBHXrE"

logging.basicConfig(level=logging.INFO)

PROMOZIONI = {
    "WindTre": ["WindTre Full 5G - 200GB a 7,99€/mese", "WindTre Young - 100GB a 6,99€/mese"],
    "TIM": ["TIM Power - 150GB a 9,99€/mese", "TIM Young - 100GB a 7,99€/mese"],
    "Vodafone": ["Vodafone Special - 100GB a 7,99€/mese", "Vodafone RED - 200GB a 9,99€/mese"],
    "Fastweb": ["Fastweb Mobile - 150GB a 7,95€/mese", "Fastweb NeXXt - 200GB a 9,95€/mese"],
    "Optima": ["Optima Comfort - 100GB a 5,95€/mese", "Optima Top - 200GB a 8,95€/mese"],
    "Iliad": ["Iliad Giga 150 - 150GB a 7,99€/mese", "Iliad Dati - 300GB a 13,99€/mese"],
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(nome, callback_data=nome)]
        for nome in PROMOZIONI.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_text = "📱 *Benvenuto!* Seleziona un operatore per vedere le migliori promozioni attuali."
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    operatore = query.data
    offerte = PROMOZIONI.get(operatore, [])
    testo = f"📢 Offerte attuali di {operatore}:\n\n" + "\n".join(f"🔹 {offerta}" for offerta in offerte)
    await query.edit_message_text(text=testo)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_query))
    print("✅ Bot avviato.")
    app.run_polling()
