from logging import Filter
from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, ConversationHandler, CallbackQueryHandler

def result(list, z):
    if z == '0':
        return int(list[0]) + int(list[1])
    elif z == '1':
        return int(list[0]) - int(list[1])
    elif z == '2':
        return int(list[0]) * int(list[1])
    else:
        return int(list[0]) / int(list[1])
    
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}. Для вызова калькулятора введи /calc')

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Я смотрю ты хочешь что-то посчитать. Введи через пробел 2 числа')
    return 1

async def inputNumbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global numbers
    numbers = update.message.text.split()
    board = [[InlineKeyboardButton('+', callback_data='0'), InlineKeyboardButton('-', callback_data='1')],
             [InlineKeyboardButton('*', callback_data='2'), InlineKeyboardButton(':', callback_data='3')]]
    await update.message.reply_text('Выбери:', reply_markup=InlineKeyboardMarkup(board))
    return 2

async def operation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global res
    que = update.callback_query
    var = que.data
    que.answer()
    res = result(numbers, var)
    await que.message.edit_text(f'Результат: {res}')

async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Пока-пока')
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token("TOKEN").build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(ConversationHandler(entry_points=[CommandHandler("calc", calc)],
                                        states={1: [MessageHandler(Filter.__text_signature__, inputNumbers)],
                                                2: [CallbackQueryHandler(operation)]},
                                        fallbacks=[CommandHandler("exit", exit)]))
    app.run_polling()

if __name__ == "__main__":
    main()