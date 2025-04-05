from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from analysis import get_top_matches

TOKEN = "ВАШ_ТОКЕН"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я покажу лучшие матчи для ставок.")

async def best(update: Update, context: ContextTypes.DEFAULT_TYPE):
    matches = get_top_matches()
    if not matches:
        await update.message.reply_text("Нет подходящих матчей сейчас.")
        return
    text = "\n\n".join([f"{m['teams']}\nКоэфф: {m['odds']}, Шанс: {m['score']}%" for m in matches])
    await update.message.reply_text("Рекомендуемые матчи:\n\n" + text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("best", best))
app.run_polling()