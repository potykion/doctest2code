import os

from aiohttp import web

from doctest2code.app import create_app

if __name__ == '__main__':
    web.run_app(
        create_app(),
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080))
    )
