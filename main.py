import asyncio
from telethon import TelegramClient, events

api_id = '28880373'
api_hash = '8ac84cce1fec1e3aeb2afc2140cb85e5'
phone_number = '+48507942372'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone_number)

    @client.on(events.NewMessage)
    async def handle_new_message(event):
        if 'missed call' in event.raw_text.lower() or 'missed video call' in event.raw_text.lower():
            sender = await event.get_sender()
            sender_id = sender.id
            await client.send_message(sender_id, 'Извините, я не могу сейчас ответить на звонок. Пожалуйста, оставьте сообщение.')

    print("Бот автоответчик запущен...")
    await client.run_until_disconnected()

# Запуск основной функции
asyncio.run(main())