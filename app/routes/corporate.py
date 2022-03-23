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
    """
        this is a Post route which interacts with the database to create a new corporate entry.
        We take the corporate details and pass it to CorporateManager where it will be stored in db.
        See implementation at manager -> corporate_manager.py.

        :params request: request object
        :return: response object in json format

    """
    payload = request.custom_json()
    _response = await CorporateManager.create_corporate(payload)
    return send_response(_response)

@corporate.route("/corporate/<name:string>",methods=['GET'])
async def get_corporate_by_name(request: Request,name):
    payload = name
    _response = await CorporateManager.get_corporate_by_name(payload)
    _response['id'] = str(_response['id'])
    return send_response(_response)

@corporate.route("/presignedurl",methods=['GET'])
async def get_presigned_url(request: Request):
    """
        this is a Get Api endpoint which when hit will call a function
        named generate_presigned_url See implementation at manager -> corporate_manager.py.
        which will then return us a presigned url.
    """

    query_params = request.request_params()
    query_params = {
            "Key": query_params.get('filename'),
            "ContentType": query_params.get('ContentType')
        }
    response = await CorporateManager.generate_presigned_url(**query_params)
    return send_response(response)