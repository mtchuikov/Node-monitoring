import asyncio
from aiohttp import web
from app import api

app = web.Application()
app.add_routes([*api.router()])

async def main():
    await asyncio.gather(
        web._run_app(app, host="localhost", port="8080"),
    )

if __name__ == "__main__":
    asyncio.run(main())

