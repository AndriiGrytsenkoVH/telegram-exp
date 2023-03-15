from telethon import TelegramClient
from constants import api_hash, api_id
from datetime import datetime, timedelta

client = TelegramClient('anon', api_id, api_hash)

async def get_messages(channel, days):
    start_date = datetime.now() - timedelta(days=days)
    start_date = datetime(*start_date.timetuple()[:3])
    my_gen = client.iter_messages(channel, reverse=True, offset_date=start_date)
    return [message.raw_text async for message in my_gen][::-1]

# with client:
#     client.loop.run_until_complete(main())
        