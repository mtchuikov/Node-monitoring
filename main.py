import asyncio
from aiohttp import web
from app import api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = web.Application()
app.add_routes([*api.router()])

engine = create_engine(r'sqlite:///server_data.db', echo=True)
session = sessionmaker(bind=engine)()

async def main():
    await asyncio.gather(
        web._run_app(app, host="localhost", port="8080"),
    )

if __name__ == "__main__":
    asyncio.run(main())

