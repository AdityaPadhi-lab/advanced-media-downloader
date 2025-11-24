import os
import aiofiles
import aiohttp
from pathlib import Path
import hashlib

DOWNLOAD_DIR = Path("/data/downloads")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

async def download_url(session: aiohttp.ClientSession, url: str, outpath: Path):
    async with session.get(url) as r:
        r.raise_for_status()
        async with aiofiles.open(outpath, "wb") as f:
            async for chunk in r.content.iter_chunked(1_048_576):
                await f.write(chunk)

    h = hashlib.sha256()
    async with aiofiles.open(outpath, "rb") as f:
        while True:
            chunk = await f.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()
