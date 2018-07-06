from aiohttp import web
import jinja2

from doctest2code.utils import doctest_to_code

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("./templates"),
    enable_async=True,
)


async def index(request: web.Request) -> web.Response:
    context = {
        "doctest": request.cookies.get("doctest"),
        "code": request.cookies.get("code")
    }

    if request.method == "POST":
        data = await request.post()
        context["doctest"] = data.get("doctest")
        context["code"] = doctest_to_code(context["doctest"])

    template = env.get_template("index.html")
    html = await template.render_async(**context)

    response = web.Response(body=html, content_type="text/html")
    response.set_cookie("doctest", context.get("doctest"))
    response.set_cookie("code", context.get("code"))

    return response


def create_app() -> web.Application:
    app = web.Application()
    app.add_routes([
        web.get("/", index),
        web.post("/", index)
    ])
    return app
