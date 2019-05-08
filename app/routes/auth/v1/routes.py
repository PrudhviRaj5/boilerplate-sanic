from sanic import Blueprint
from sanic import response
from sanic.exceptions import ServerError
from app.routes.auth import controller
from app.config import CONFIG

auth_v1_bp = Blueprint('auth', url_prefix='py-api/auth/v1/')


@auth_v1_bp.route('/login', methods=['POST'])
async def login(request):
    u_name = request.json['username']
    u_pass = request.json['password']
    res = controller.login(u_name, u_pass)
    return response.json({'payload': res})


@auth_v1_bp.route('/create_user', methods=['POST'])
async def create_user(request):
    u_name = request.json['username']
    u_pass = request.json['password']
    res = controller.create_user(u_name, u_pass)
    return response.json({'payload': res})


@auth_v1_bp.route('/create_role', methods=['POST'])
async def create_role(request):
    role_name = request.json['name']
    res = controller.create_role(role_name)
    return response.json({'payload': res})


@auth_v1_bp.route('/create_organization', methods=['POST'])
async def create_organization(request):
    org_name = request.json['name']
    org_domain = request.json['domain']
    res = controller.create_organization(org_name, org_domain)
    return response.json({'payload': res})


@auth_v1_bp.route('/verify', methods=['GET'])
async def verify_token(request):
    token = request.headers['session_token']
    res = controller.verify_token(token)
    return response.json({'payload': res})
