import asyncio
import aiohttp
import multiprocessing
import os
from .download_tasks import download_url, DOWNLOAD_DIR

BACKEND = os.environ.get("BACKEND_URL", "http://server:8000")

async def run_job(job):
    url = job["source_url"]
    tid = job["task_id"]
    outname = DOWNLOAD_DIR / f"{tid}.bin"
    async with aiohttp.ClientSession() as s:
        checksum = await download_url(s, url, outname)
        await s.post(f"{BACKEND}/api/tasks/{tid}/complete", json={"path": str(outname), "checksum": checksum})

async def poll_loop():
    import aiohttp
    while True:
        try:
            async with aiohttp.ClientSession() as s:
                r = await s.get(f"{BACKEND}/api/tasks/pending")
                if r.status == 200:
                    jobs = await r.json()
                    if jobs:
                        tasks = [run_job(j) for j in jobs]
                        await asyncio.gather(*tasks)
        except Exception:
            pass
        await asyncio.sleep(3)

if __name__ == '__main__':
    PROCS = int(os.environ.get("WORKER_PROCS", "2"))
    procs = []
    for _ in range(PROCS):
        p = multiprocessing.Process(target=lambda: asyncio.run(poll_loop()))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
