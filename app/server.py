from sanic import Sanic
from sanic import response
from sanic.log import logger as log
from sanic.exceptions import ServerError
import time

from app.config import CONFIG

from app.routes.auth.v1.routes import (
    auth_v1_bp as auth_v1_routes,
)
from app.routes.module_1.v1.routes import (
    module_1_v1_bp as module_1_v1_routes,
)
from app.routes.module_1.v2.routes import (
    module_1_v2_bp as module_1_v2_routes,
)


app = Sanic(__name__, load_env='B2B_APP_')
app.config.from_object(CONFIG)

# These routes will be ignored by middlewares
# ----------------------------------------------- #
# sample Apis
# ----------------------------------------------- #

@app.route("/")
async def test_async(request):
    time.sleep(3)
    return response.json({"test": True})


@app.route("/sync", methods=['GET', 'POST'])
def test_sync(request):
    return response.json({"test": True})


@app.route("/dynamic/<name>/<i:int>")
def test_params(request, name, i):
    return response.text("yeehaww {} {}".format(name, i))


@app.route("/await")
async def test_await(request):
    import asyncio
    await asyncio.sleep(5)
    return response.text("I'm feeling sleepy")

# ----------------------------------------------- #
# redirect request
# ----------------------------------------------- #

@app.route('/test_redirect', methods=['GET', 'POST'])
def handle_request(request):
    return response.redirect('/redirect')

@app.route('/redirect')
async def test(request):
    return response.json({"Redirected": True})

# ----------------------------------------------- #
# handle files
# ----------------------------------------------- #

@app.route("/file")
async def test_file(request):
    return await response.file(os.path.abspath("setup.py"))


@app.route("/file_stream")
async def test_file_stream(request):
    return await response.file_stream(os.path.abspath("setup.py"),
                                      chunk_size=1024)

# ----------------------------------------------- #
# Exceptions
# ----------------------------------------------- #

@app.route("/exception")
def exception(request):
    raise ServerError("It's dead jim")

@app.exception(ServerError)
async def test(request, exception):
    return response.json({"exception": "{}".format(exception), "status": exception.status_code},
                         status=exception.status_code)


# ----------------------------------------------- #
# Read from request
# ----------------------------------------------- #

@app.route("/json")
def post_json(request):
    return response.json({"received": True, "message": request.json})


@app.route("/form")
def post_form_json(request):
    return response.json({"received": True, "form_data": request.form, "test": request.form.get('test')})


@app.route("/query_string")
def query_string(request):
    return response.json({"parsed": True, "args": request.args, "url": request.url,
                          "query_string": request.query_string})


# ----------------------------------------------- #
# Specify All PRE-REQUEST middlewares here
# ----------------------------------------------- #
@app.middleware('request')
async def halt_request(req):
    # specify functions to execute before reaching the route
    # like modify req headers, etc
    pass


# ----------------------------------------------- #
# Specify All ROUTES here
# ----------------------------------------------- #

app.blueprint(auth_v1_routes)
app.blueprint(module_1_v1_routes)
app.blueprint(module_1_v2_routes)

# ----------------------------------------------- #
# Specify All POST-REQUEST middlewares here
# ----------------------------------------------- #
@app.middleware('response')
async def halt_response(req, res):
    # specify functions to execute after reaching the route
    # like modify response, etc
    pass
