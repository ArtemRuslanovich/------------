import asyncio
from telethon import TelegramClient, events

api_id = '28880373'
api_hash = '8ac84cce1fec1e3aeb2afc2140cb85e5'
phone_number = '+48507942372'

client = TelegramClient(None, api_id, api_hash)

async def main():
    await client.start(phone_number)

    @client.on(events.NewMessage(pattern='(missed call|missed video call)', flags=events.NewMessage.Incoming))
    async def handle_missed_call(event):
        sender = await event.get_sender()
        sender_id = sender.id
        message = 'Здравствуйте 👋, это сообщение отправлено автоматом 🤖, в данный момент я не абонент 😴, оставьте сообщение👇.'
        await client.send_message(sender_id, message)

    print("Бот автоответчик запущен...")
    await client.run_until_disconnected()

asyncio.run(main())
