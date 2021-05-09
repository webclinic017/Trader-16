from btrader import BTrader
from config.config import *
from telegram.ext import *
import bank
import options


def help_command(update, context):
    update.message.reply_text(help_message)


def alarm(context: CallbackContext) -> None:
    job = context.job
    trader = BTrader(100, job.name)
    revenue = trader.run()
    text = trader.response.get_response()
    if text:
        text += '\n' + revenue
    elif notify_when_there_is_no_signal:
        text = non
    context.bot.send_message(job.context, text=text)


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def set_timer(update, context):
    chat_id = update.message.chat_id

    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_repeating(
        alarm, telegram_hour, context=chat_id, name=str(chat_id))

    update.message.reply_text(start_message)


def unset(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = stop_message if job_removed else off_message
    update.message.reply_text(text)


def setbar(update, context):
    try:
        val = context.args[0]
        if val not in ['1', '3', '5', '15', '30', '60']:
            update.message.reply_text(bar_error_message)
            return
        chat_id = update.message.chat_id
        options.set_opt(chat_id, bar=time_frames[val])
        update.message.reply_text(bar_message)
    except:
        update.message.reply_text(bar_error_message)


def setcash(update, context):
    try:
        val = int(context.args[0])
        if val <= 0:
            update.message.reply_text(cash_error_message)
            return
        chat_id = update.message.chat_id
        bank.set_cash(chat_id, val)
        update.message.reply_text(cash_message)
    except:
        update.message.reply_text(cash_error_message)


def cash(update, context):
    chat_id = update.message.chat_id
    val = bank.get_cash(chat_id)
    if val:
        text = get_cash_message + str(val)
        update.message.reply_text(text)
    else:
        update.message.reply_text(no_cash_message)


def per(update, context):
    chat_id = update.message.chat_id
    try:
        val = int(context.args[0])
        if val <= 0 and val > 100:
            update.message.reply_text(cash_error_message)
            return
        chat_id = update.message.chat_id
        options.set_opt(chat_id, per=val/100)
        update.message.reply_text(cash_message)
    except:
        update.message.reply_text(cash_error_message)


def info(update, context):
    chat_id = update.message.chat_id
    csh = bank.get_cash(chat_id)
    opt = options.get_opt(chat_id)
    text = get_ticker_message + ticker + '\n'

    if csh:
        text += get_cash_message + str(csh) + '\n'
    if opt:
        text += get_bar_message + str(opt['bar']) + '\n'
        text += get_per_message + str(opt['per'] * 100) + '% \n'

    update.message.reply_text(text)


def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(
        TELEGRAM_API_KEY, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler("start", set_timer))
    dp.add_handler(CommandHandler("stop", unset))
    dp.add_handler(CommandHandler("setbar", setbar))
    dp.add_handler(CommandHandler("setcash", setcash))
    dp.add_handler(CommandHandler("cash", cash))
    dp.add_handler(CommandHandler("setorderpercentage", per))
    dp.add_handler(CommandHandler("info", info))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
