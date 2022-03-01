from sanic import Blueprint
from torpedo import Request, send_response
from ..managers import CorporateManager
from app.validator import Validator
from app.constants import CorporateType
corporate = Blueprint("corporate", version=4)

@corporate.route("/corporate", methods=['GET'])
async def get_all_corporate(request):
    _response = await CorporateManager.get_all_cprporate()
    return send_response(_response)


@corporate.route("/corporate", methods=['POST'])
async def create_corporate(request):
    payload = request.request_params()
    Validator.mandatory_params(name=payload.get('name'), phone=payload.get('phone'), spoc_email=payload.get('spoc_email'),
          spoc_phone=payload.get('spoc_phone'), coupon_code=payload.get('coupon_code'), address=payload.get('address'),
    domains=payload.get('domains'), logo_url=payload.get('logo_url'), html=payload.get('html'),dashboard_url=payload.get('dashboard_url'))

    Validator.param_in_check('type', payload.get('type'), CorporateType.corporate_type.value)

    Validator.param_type_check(str, name=payload.get('name'), phone=payload.get('phone'), spoc_email=payload.get('spoc_email'),
          spoc_phone=payload.get('spoc_phone'), coupon_code=payload.get('coupon_code'), address=payload.get('address'),
          logo_url=payload.get('logo_url'), html=payload.get('html'), dashboard_url=payload.get('dashboard_url'))

    _response = await CorporateManager.create_corporate(payload)
    return send_response(_response)
