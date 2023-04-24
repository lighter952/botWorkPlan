from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from table_parsing import get_list_of_employees
from table_parsing import get_plan_by_employee_number
import logging
from print import get_mounth_by_number



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
userss = {441488533: 15}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    # user = update.effective_user
    print(update.message.chat)
    await update.message.reply_text("Hello, " + update.message.from_user.first_name + '!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Print your number!")


async def all_month_plan_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a all month plan"""
    await update.message.reply_text("All mouth plan")
    user_id = update.message.from_user.id
    await update.message.reply_text(get_mounth_by_number(userss.get(user_id)))


async def tomorrow_plan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send o tomorrow plan"""



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    print("New user: user ID is ", update.message.from_user.id)
    await update.message.reply_text("Hi in my bot")


def bot_run() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token('5899902676:AAFN2jrQKzdwzrGTLynqbw6aAyOxtsyaXuA').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("all_month", all_month_plan_command))
    application.add_handler(CommandHandler("tomorrow_plan", tomorrow_plan))
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
