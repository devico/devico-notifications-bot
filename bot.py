import requests
import telegram
import os
import logging
import time


logging.basicConfig(format=u'%(process)d %(LevelName)s %(message)s')
logger = logging.getLogger('BotLogger')
logger.setLevel(logging.INFO)


telegram_token = os.getenv("TELEGRAM_TOKEN")


def request_api(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def send_bot_message(negative_attempt, bot, chat_id):
    bot.send_message(chat_id=chat_id, text="У вас проверили работу 'Отправляем уведомления о проверке работ'")
    if negative_attempt:
        bot.send_message(chat_id=chat_id, text="К сожалению, в работе нашлись ошибки.")
    else:
        bot.send_message(chat_id=chat_id, text="Преподавателю понравилось, можно приступать к следующему уроку.")


def main():
    url = 'https://dvmn.org/api/long_polling/'
    devman_token = os.getenv("DEVMAN_TOKEN")
    chat_id = 323863021
    headers = {"Authorization": devman_token}
    params = {}

    logger.info('Бот запущен!')

    while True:
        try:
            data = request_api(url, headers=headers, params=params)
        except requests.exceptions.ReadTimeout as e:
            logging.error(e)
            logger.info('Бот упал с ошибкой:')
            logger.info(e)
            continue
        except requests.exceptions.ConnectionError as errc:
            logging.error("Error Connecting:", errc)
            logger.info('Бот упал с ошибкой:')
            logger.info(errc)
            time.sleep(10)

        if data['status'] == 'found':
            last_tsmp = data['last_attempt_timestamp']
            params = {'timestamp': last_tsmp}
            negative_attempt = data['new_attempts']['is_negative']
            send_bot_message(negative_attempt, bot, chat_id)
        else:
            tsmp = data['timestamp_to_request']
            params = {'timestamp': tsmp}


if __name__ == '__main__':
    bot = telegram.Bot(token=telegram_token)
    chat_id = 323863021


    class BotLogsHandler(logging.Handler):

        def emit(self, record):
            log_entry = self.format(record)
            bot.send_message(chat_id=chat_id, text=log_entry)


    logger.addHandler(BotLogsHandler())

    main()
