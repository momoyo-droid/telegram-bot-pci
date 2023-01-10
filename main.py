from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from telegram import Update
from time import time
import random as rd
import logging
import utils


async def help(update: Update, contextTypes: ContextTypes.DEFAULT_TYPE):
    t = [
        "type / in chat and my commands will appear",
        "\n",
        "found any problem? talk to my owner @ana0oliveira on telegram\n",
        "https://github.com/momoyo-droid/telegram-bot-pci\n"
    ]
    s = "".join(t)
    await update.message.reply_text(s)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello outsider! It's lost? Type /help there and I'll see what I can do for you 😘."
    )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Sorry, I didn't understand that command.")


async def fwd(update: Update, context: ContextTypes.DEFAULT_TYPE):

    while True:
        msgID = rd.randint(1, utils.MAX_MSG_FWD)

        await context.bot.forwardMessage(
            chat_id=update.effective_chat.id,
            from_chat_id=utils.TOKEN_GROUP, message_id=msgID)
        break


async def reverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    w = update.message.text[8:]
    await update.message.reply_text(w[::-1])


async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(utils.getRandomQuestion())


def main():
    application = ApplicationBuilder().token(utils.API_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('reverse', reverse))
    application.add_handler(CommandHandler('fwd', fwd))
    application.add_handler(CommandHandler('question', question))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    main()
