import asyncio
from pyrogram import Client
from .config import settings
from pyrogram.types import Message
import aiohttp

RUNNING = set()

def track_task(coro):
    t = asyncio.create_task(coro)
    RUNNING.add(t)
    t.add_done_callback(lambda _: RUNNING.discard(t))
    return t

async def safe_download_and_enqueue(client: Client, message: Message, url: str):
    try:
        async with aiohttp.ClientSession() as s:
            payload = {"source_url": url, "chat_id": message.chat.id, "msg_id": message.id}
            r = await s.post(f"{settings.BACKEND_URL}/api/tasks", json=payload)
            if r.status == 201:
                await message.reply("✅ Task created — processing in worker pool.")
            else:
                txt = await r.text()
                await message.reply(f"❌ Failed to create task: {txt}")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")
