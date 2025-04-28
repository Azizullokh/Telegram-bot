import logging
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7561170378:AAGXzAcge9u6MpiUixnuiBlEcUB91lS3tqU'

usernames = [
    '@mgg_3811', '@Shrzdvna27', '@MoonliitRose', '@lvssrrw', '@ergwbyv_n',
    '@xlmrzyva_m', '@toshxojayev03', '@mub1shaa'
]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['/callall', '/help']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    await update.message.reply_text('Nima gap! Bot ishlayapti. Tanlang komandalardan otam:', reply_markup=reply_markup)

async def is_user_admin(update: Update) -> bool:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    member = await update.effective_chat.get_member(user_id)
    return member.status in ['administrator', 'creator']

async def callall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if update.effective_chat.type not in ["group", "supergroup"]:
        await update.message.reply_text("Bu buyruq faqat guruhlarda ishlaydi!")
        return

    if not await is_user_admin(update):
        await update.message.reply_text("Faqat adminlar /callall ishlata oladi.")
        return

    chunk_size = 7
    for i in range(0, len(usernames), chunk_size):
        chunk = usernames[i:i + chunk_size]
        text = ' '.join(chunk)
        await context.bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)
        await asyncio.sleep(2)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('callall', callall))

    print("Bot ishlayapti...")
    app.run_polling()

if __name__ == '__main__':
    main()
