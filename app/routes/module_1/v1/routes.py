from sanic import Blueprint
from sanic import response
from sanic.exceptions import ServerError
from app.routes.module_1 import controller
from app.config import CONFIG

module_1_v1_bp = Blueprint('module_1_v1', url_prefix='py-api/v1/module_1')


@module_1_v1_bp.route('/get_data', methods=['GET'])
async def get_mem(request):
    data = await controller.get_data()
    return response.json({'payload': data})
