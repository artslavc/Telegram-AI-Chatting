from pyrogram import Client, idle, filters
from pyrogram.types import Message
from datetime import datetime as DT
from pyrogram.handlers import MessageHandler
import random
import pyrogram.utils

pyrogram.utils.get_peer_type = lambda peer_id: "channel" if str(peer_id).startswith("-100") else "user"

from g4f_engine import get_neuro_comment

async def handle_text_message(client, message):
    message_group = await client.get_messages(message.chat.id, message.id)

    if random.choice([True, False, False, False]):
        comment = await get_neuro_comment(message_group.text.replace('\n', ' '))
        print(f"[!] Сообщение: {message_group.text}\n"
              f"[*] Ответ от Chat GPT: {comment}")
        await message.reply(comment)

async def my_handler(client: Client, message: Message):
    try:
        if message.text:
            await handle_text_message(client, message)
    except Exception as e:
        pass

async def start_thread(client, target_groups):
    for group_id in target_groups:
        if '\n' in group_id or ' ' in group_id:
            group_id = group_id.replace('\n', ''); group_id = group_id.replace(' ', '')
        client.add_handler(MessageHandler(my_handler, filters.chat(group_id)))
    await idle()