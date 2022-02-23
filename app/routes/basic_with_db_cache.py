from sanic import Blueprint
from torpedo import send_response

from ..managers import MydbManager

basic_with_db_cache = Blueprint("basic_with_db_cache", version=4)



@basic_with_db_cache.route("/users/<username:str>", methods=["GET"])
async def get_user(request,username:str):
    """
    this is an example of route which interacts with the database connection created in same service.
    We are connecting with identity db on staging for this service. See model implementation at models -> user.py.
    It also uses caching support defined in caches -> user.py.
    """
    payload = username
    _response = await MydbManager.get_user(payload)
    return send_response(_response)

@basic_with_db_cache.route("/users", methods=["POST"])
async def create_user(request):
    payload = request.args
    _response = await MydbManager.create_user(payload)
    return send_response(_response)

@basic_with_db_cache.route("/users/<name:str>", methods=['DELETE'])
async def delete_user(request, name:str):
    payload=name
    _response = await MydbManager.delete_user(payload)
    return send_response(_response)