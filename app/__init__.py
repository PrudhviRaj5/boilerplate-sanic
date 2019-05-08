""" App entry point. """
import os
from sanic.log import logger as log


def create_app():
    """ Function for bootstrapping sanic app. """

    from app.server import app

    # ----------------------------------------------- #
    # Run Server
    # ----------------------------------------------- #

    # @app.listener('before_server_start')
    # async def before_start(app, loop):
    #     log.info("SERVER STARTING")

    # @app.listener('after_server_start')
    # async def after_start(app, loop):
    #     log.info("Successfully Started Server! :)")

    # @app.listener('before_server_stop')
    # async def before_stop(app, loop):
    #     log.info("SERVER STOPPING")

    # @app.listener('after_server_stop')
    # async def after_stop(app, loop):
    #     log.info("Stopped Server! :(")


    # starting app in the port 3344
    app.go_fast(
    # app.run(
        host='0.0.0.0', port=3344,
        debug=True,
        workers=2
        # workers=os.cpu_count()
    )
