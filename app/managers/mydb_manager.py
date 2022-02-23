from torpedo.wrappers import ORMWrapper
from ..models import Mydb
from ..models import User
class MydbManager:

    @classmethod
    async def get_user(cls, payload):
        username = payload
        user = await ORMWrapper.get_by_filters(Mydb, {"username": username})
        user = await user[0].to_dict()
        return user

    @classmethod
    async def create_user(cls, payload):
        payload["id"] = int(payload.get("id"))
        print(payload)

        new_user = await ORMWrapper.create(Mydb, payload)
        new_user = await new_user.to_dict()
        return new_user

    @classmethod
    async def delete_user(cls, payload):
        await Mydb.filter(username=payload).delete()
        return {"message": "deleted"}

