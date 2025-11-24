import os

# FIX WRONG SYSTEM UNIX TIME
os.environ["PYROGRAM_TIME_OFFSET"] = "-31509973"
os.environ["TZ"] = "UTC"

from pyrogram import Client, filters
from .config import settings
from .handlers import on_message, start_cmd

app = Client(
    "media_bot",
    api_id=settings.API_ID,
    api_hash=settings.API_HASH,
    bot_token=settings.BOT_TOKEN,
    workdir=".",
    sleep_threshold=60
)

@app.on_message()
async def _on_message(client, message):
    await on_message(client, message)

@app.on_message(filters.command("start"))
async def _start(client, message):
    await start_cmd(client, message)

if __name__ == "__main__":
    app.run()
