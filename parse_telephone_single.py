import time

from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
import asyncio, random, logging
from telethon import functions
import transliterate
from python_socks import ProxyType
from transliterate import translit

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(__file__ + '.log', encoding='UTF-8', mode='w')])

a = ord('А')
alphabet = [chr(i) for i in range(a, a + 64)]

# Загружаем IDs из файла в множество
with open('channel_ids.txt', 'r') as f:
    existing_ids = set(f.readlines())


async def search_channels(client, query):
    last_id = None
    try:

        # Ищем чаты и каналы по запросу
        results = await client(functions.contacts.SearchRequest(q=query, limit=100))
        logging.info(results)
        for result in results.chats:
            await asyncio.sleep(random.randint(25, 35))
            # Проверка является ли результат каналом (не супергруппой) и имеет ли он более 800 подписчиков
            if not result.megagroup and result.participants_count > 800 and 'Channel' in str(result):
                channel_id_str = '-100' + str(result.id) + '\n'
                try:
                    message = await client.get_messages(result.id, 1)
                    first_char = message[-1].text[0] if message and message[0].text else None
                    last_char = message[-1].text[-1] if message and message[0].text else None

                except Exception as e:
                    logging.info(f"Ошибка при получении сообщения: {e}")
                    first_char = None
                finally:
                    await asyncio.sleep(random.randint(7, 20))
                if (first_char or
                    last_char or
                    result.title[0] or
                    result.title[2]) in alphabet \
                        and channel_id_str not in existing_ids:
                    with open('channel_names.txt', 'a') as f:
                        f.write(result.username + '\n')
                    with open('channel_ids.txt', 'a') as f:
                        f.write(channel_id_str)

        # Установка последнего даты, ID и access_hash для следующего запроса
        # last_id = results[-1].id
        # задержка во избежание частых вызовов API
    except FloodWaitError as e:
        wait_time = e.seconds
        logging.error(f"Нужно подождать {wait_time} секунд.")
        await asyncio.sleep(wait_time)  # Подождите рекомендованное время, прежде чем повторить попытку


# Ваши данные для авторизации
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'
acc = {
    "api_id": 26916777, "api_hash": "c4abeac38a9fad71aaafaff79c112cc4", "phone_number": "+66994011738",
    'my_proxy': {'proxy_type': ProxyType.SOCKS5, 'addr': '185.192.109.201', 'port': 60417, 'username': '25bd65a195', 'password': '62c59dd5f2'}}
code_phrases = ['mama', '@mamka', 'mamulya', 'mamochka', 'moms', 'mami', 'mamasha', 'mamashka',
                'родительница', 'мамуля', 'мать', 'маманя', 'мамаша', 'мамка', 'маменька', 'матка', 'матушка',
                'родимая', 'матерь', 'река', 'мамочка', 'мамуся', 'мамусенька', 'мамулечка', 'мамусечка', 'мамушка',
                'маманюшка', 'мамашенька', 'мамашечка', 'маман', 'маманька', 'мамонька', 'мамулька', 'мамунька',
                'мамуня', 'мамуша', 'мамысь', 'мамыса', 'маточка', 'матенка', 'матушь', 'матуша', 'матуха', 'матухна',
                'матуня', 'матуничка', 'матуненька', 'матунюшка', 'матуся', 'матусенька', 'матуля', 'матуличка', 'матя',
                'матика', 'матонька', 'матынька', 'матунька', 'мачка', 'родимая матушка']
code_phrases2 = []
code_phrases3 = ['влечение', 'увлечение', 'привязанность', 'склонность', 'наклонность', 'слабость', 'страсть',
                 'пристрастие', 'преданность', 'тяготение', 'мания', 'симпатия', 'верность', 'благоволение',
                 'благорасположение', 'благосклонность', 'доброжелательство', 'предрасположение', 'вожделение',
                 'афродита', 'пристрастность', 'обожание', 'влюбленность', 'роман', 'интрига',
                 'эрос', 'шашни', 'филиа', 'приверженность', 'страстишка', 'шуры-муры', 'интрижка', 'пассия',
                 'человеколюбие', 'чувство', 'ласка', 'любава', 'неравнодушие', 'бхакти', 'вкус', 'расположение',
                 'тяга', 'связь', 'любовная связь', 'близкие отношения', 'интимные отношения', 'амуры',
                 'нежная страсть', 'сердечные дела', 'нежное чувство', 'лямур', 'крутой лямур', 'возлюбленная',
                 'возлюбленный', 'люба', 'любовь-морковь', 'слабая струна', 'гетеризм', 'сторгэ', 'боголюбие',
                 'боголюбство', 'заноза', 'сердечная склонность',
                 ]


def main():
    try:
        my_proxy = acc.get('my_proxy', None)
        client = TelegramClient(f'{acc["phone_number"]}_telethon', acc["api_id"], acc["api_hash"], proxy=my_proxy)
        client.start(int(acc["phone_number"]), password='Wf52')
        client.connect()
        with open('russian_edit.txt', 'r+', encoding='utf-8', errors='ignore') as f:
            for line in f:
                try:
                    word = line.strip()
                    code_phrases2.append(word)
                except UnicodeDecodeError as e:
                    print(f"Произошла ошибка декодирования: {e}")
                    # Можно добавить дополнительный код для обработки ошибки или просто продолжить выполнение цикла
                    continue
            f.seek(0)
            lines = f.readlines()
            logging.info(lines[0:10])
            iteration_count = -1
            for q in code_phrases2[0::5]:
                iteration_count += 1
                logging.info(f'{q}')
                time.sleep(30)
                f.seek(0)
                f.writelines(lines)
                try:
                    text = translit(q, language_code='ru', reversed=True)
                    client.loop.run_until_complete(search_channels(client=client, query="@" + text))
                except Exception as e:
                    logging.error(f'An unexpected error occurred: {e}', exc_info=True)
                # Здесь определите, какую запись вы хотите удалить.
                # Например, если вы хотите удалить строку, содержащую "арбуз":
                # Удалите запись из списка.
                f.seek(0)
                lines = lines[5:]
                # lines.remove(record_to_delete)
                f.seek(0)
        time.sleep(150)
    except (ConnectionError, FloodWaitError) as e:
        logging.warning(f'Connection error: {e}')
        logging.info('Reconnecting in 60 seconds...')
        time.sleep(60)
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}', exc_info=True)
    finally:
        main()


if __name__ == "__main__":
    while True:
        try:
            main()  # Здесь вызывайте вашу функцию или скрипт
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Restarting the script in 10 seconds...")
            time.sleep(60)  # Подождите 10 секунд перед перезапуском
