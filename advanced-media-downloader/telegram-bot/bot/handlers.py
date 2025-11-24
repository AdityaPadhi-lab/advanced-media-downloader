import re
from pyrogram import filters
from pyrogram.types import Message
from .streamer import track_task, safe_download_and_enqueue

DL_LINK_RE = re.compile(r"https?://t\.me/[^\s]+")

async def on_message(client, message: Message):
    text = message.text or message.caption or ""
    if not text:
        return
    m = DL_LINK_RE.search(text)
    if m:
        url = m.group(0)
        await message.reply("Queued for download 📥")
        track_task(safe_download_and_enqueue(client, message, url))

async def start_cmd(client, message: Message):
    await message.reply("Hi — advanced media downloader bot running.")
