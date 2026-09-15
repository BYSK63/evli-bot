from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
TOKEN = "8746275911:AAHf1gXN02bvGm4iFBcBRzy1OdC1z4VeFNw"
KELIMELER = ["evli çiftiz", "evli ciftiz", "evli çift", "evliyiz", "evli cift"]
async def kontrol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    try:
        m = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
        if m.status in ['administrator', 'creator']:
            return
    except:
        pass
    text = update.message.text.lower()
    for k in KELIMELER:
        if k in text:
            return
    try:
        await update.message.delete()
    except:
        pass
app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, kontrol))
app.run_polling()
