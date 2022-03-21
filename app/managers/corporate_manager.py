from ..models import CorporateService
from torpedo.exceptions import HTTPInterServiceRequestException
from torpedo.wrappers import ORMWrapper
from ..service_clients import data_service
import datetime

# import asyncio
# from aiobotocore.session import get_session
# async def test():
#     session = get_session()
#     async with session.create_client('s3', region_name='ap-south-1') as client:
#         url = await client.generate_presigned_url(ClientMethod='put_object', Params={'Bucket': '1mg-gumlet','Key': 'test_file'}, ExpiresIn=3600,HttpMethod='PUT')
#         print(url)
#         return url


async def uuid_tostring(payload):
    for object in payload:
        object['id'] = str(object['id'])
    return payload

async def date_to_str(payload):
    for object in payload:
        object['created_at'] = str(object['created_at'])
    return payload

class CorporateManager:

    @classmethod
    async def create_corporate(cls, payload):
        payload['created_at'] = str(datetime.date.today())
        payload['updated_at'] = str(datetime.date.today())
        static_content_response = await data_service.StaticClient.create_static_content(payload)
        if static_content_response == 200:
            _response = await ORMWrapper.create(Corporate, payload)
            new_user = await _response.to_dict()
            new_user['created_at'] = str(new_user['updated_at'])
            new_user['updated_at'] = str(new_user['updated_at'])
            return new_user
        else:
            raise HTTPInterServiceRequestException("failed to upload HTML", status_code=static_content_response)

    @classmethod
    async def get_all_corporate(cls):
        _result = await ORMWrapper.raw_sql("SELECT * FROM corporate_service ")
        # _result = await ORMWrapper.get_by_filters(CorporateService, offset=0, limit=10, filters=None)
        _result = await uuid_tostring(_result)
        _result = await date_to_str(_result)
        return _result

    @classmethod
    async def get_corporate_by_name(cls, payload):
        print(payload)
        _result = await ORMWrapper.get_by_filters(CorporateService, filters={'name': payload})
        _result = await _result[0].to_dict()
        return _result
