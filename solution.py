# Импортируем необходимые классы.
# ник бота в тг -> @datetime_by_coding_lover_bot
import logging
import datetime
from telegram.ext import Application, MessageHandler, filters, CommandHandler


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
BOT_TOKEN = '7844700878:AAHAUHAi2FlgAwC9IWoanAvqMfGv02p3Oqo'


# Определяем функцию-обработчик сообщений.
# У неё два параметра, updater, принявший сообщение и контекст - дополнительная информация о сообщении.
async def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    await update.message.reply_text(f'Я получил сообщение {update.message.text}')


async def time(update, context):
    await update.message.reply_html(str(datetime.datetime.now().time()))


async def date(update, context):
    await update.message.reply_html(str(datetime.datetime.now().date()))


def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    # Регистрируем обработчик в приложении.
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("date", date))

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()

