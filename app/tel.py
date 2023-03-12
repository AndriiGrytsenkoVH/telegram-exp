from telethon import TelegramClient
# import configparser

# config = configparser.ConfigParser()
# config.read("config.ini")

# api_id = config['Telegram']['api_id']
# api_hash = config['Telegram']['api_hash']
# api_hash = str(api_hash)

from app.config import api_hash, api_id

client = TelegramClient('anon', api_id, api_hash)


async def get_messages(channel, n):
    # result = []
    # async for message in client.iter_messages(channel, limit=n):
    #     result.append(message.text)
    my_gen = client.iter_messages(channel, limit=n)
    return [message.text async for message in my_gen]





# with client:
#     client.loop.run_until_complete(get_messages())