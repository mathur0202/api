from sanic import Blueprint
from torpedo import Request, send_response
from ..managers import CorporateManager
from ..utils import validator
from ..schema import Schema
corporate = Blueprint("corporate", version=4)


@corporate.route("/corporate", methods=['GET'])
async def get_all_corporate(request):
    _response = await CorporateManager.get_all_corporate()
    return send_response(_response)


@corporate.route("/corporate", methods=['POST'])
@validator(schema=Schema.corporate_schema)
async def create_corporate(request: Request):
    payload = request.custom_json()
    _response = await CorporateManager.create_corporate(payload)
    return send_response(_response)

@corporate.route("/corporate/<name:string>",methods=['GET'])
async def get_corporate_by_name(request: Request,name):
    payload = name
    _response = await CorporateManager.get_corporate_by_name(payload)
    _response['id'] = str(_response['id'])
    return send_response(_response)
