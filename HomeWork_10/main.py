from logging import Filter
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, ConversationHandler
from random import randint

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет {update.effective_user.first_name}. Для старта игры - /start. Для выхода - /exit')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot, player, table
    bot = 0
    player = 1
    table = 31
    await update.message.reply_text(f'Ну что, {update.effective_user.first_name}, давай начнем!'
                                     'Правила простые. Есть 31 конфета. Каждый из нас берет по очереди от 1 до 9 конфет. Побеждает тот кто забрал последние конфеты')
    await update.message.reply_text(f'{update.effective_user.first_name} ходи. Введи сколько конфет берешь со стола')
    return 1

async def operation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot, player, table
    if table > 0:
        value = number(update.message.text)
        if 1 <= value <= 9 and check_table(table, value):
            table -= value
            await update.message.reply_text(f'{update.effective_user.first_name} взял {value} конфет. На столе осталось {table} конфет')
            if table <= 0:
                await update.message.reply_text('Конфеты кончились. Напиши что-нибудь напоследок :)')
                return 2
            else:
                player = 0
                bot = 1
                await update.message.reply_text('Ход бездушной железяки')
                value = randint(1, 10)
                if check_table(table, value):
                    table -= value
                    await update.message.reply_text(f'Железка берет со стола {value} конфет. На столе осталось {table} конфет.')
                    if table <= 0:
                        await update.message.reply_text('Конфеты кончились. Напиши что-нибудь напоследок :)')
                        return 2
                    else:
                        player = 1
                        bot = 0
                        await update.message.reply_text(f'Ход переходит. Введи сколько конфет берешь со стола')
                        return 1
                else:
                    await update.message.reply_text(f'Бот оступился. Ход переходит {update.effective_user.first_name}. Введи сколько конфет берешь со стола')
                    player = 1
                    bot = 0
                    return 1
        else:
            await update.message.reply_text(f'{update.effective_user.first_name} ввёл что-то несуразное. Ход переходит железке)')
            player = 0
            bot = 1
            await update.message.reply_text('Ход бездушной железяки')
            value = randint(1, 9)
            if check_table(table, value):
                table -= value
                await update.message.reply_text(f'Железка берет со стола {value} конфет. На столе осталось {table} конфет.') 
                if table <= 0:
                    await update.message.reply_text('Конфеты кончились. Напиши что-нибудь напоследок :)')
                    return 2
                else:
                    player = 1
                    bot = 0
                    await update.message.reply_text(f'Ход переходит. Введи сколько конфет берешь со стола')
                    return 1
            else:
                await update.message.reply_text(f'Бот оступился. Ход переходит {update.effective_user.first_name}. Введи сколько конфет берешь со стола')
                player = 1
                bot = 0
                return 1
    else:
        await update.message.reply_text('Конфеты кончились. Напиши что-нибудь напоследок :)')
        return 2

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if player == 1:
        await update.message.reply_text(f'Победил {update.effective_user.first_name}! Чтобы сыграть еще раз, введи /start или /exit для выхода')
    else:
        await update.message.reply_text('Победил бот :( Чтобы сыграть еще раз, введи /start или /exit для выхода')
    return ConversationHandler.END

async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Пока-пока')
    return ConversationHandler.END

def check_table(table, count):
    temp_check = table - count
    if temp_check < 0:
        return False
    else:
        return True

def number(input):
    try:
        return int(input)
    except:
        return 0

def main():
    app = ApplicationBuilder().token("TOKEN").build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(ConversationHandler(entry_points=[CommandHandler("start", start)],
                                        states={1: [MessageHandler(Filter.__text_signature__, operation)],
                                                2: [MessageHandler(Filter.__text_signature__, msg)]},
                                        fallbacks=[CommandHandler("exit", exit)]))
    app.add_handler(CommandHandler("exit", exit))
    app.run_polling()

if __name__ == "__main__":
    main()