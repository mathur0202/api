from ..models import CorporateService
from torpedo.wrappers import ORMWrapper

class CorporateManager:

    @classmethod
    async def create_corporate(cls, payload):
        _response = await ORMWrapper.create(CorporateService, payload)
        new_user = await _response.to_dict()
        return new_user

    @classmethod
    async def get_all_cprporate(cls):
        _result = await ORMWrapper.raw_sql("SELECT name,spoc_email,type FROM corporates")
        return _result