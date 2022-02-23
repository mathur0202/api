from torpedo.db import CustomTextField, ModelUtilMixin
from tortoise import Model, fields

class Mydb(Model, ModelUtilMixin):

    id = fields.IntField(pk=True)
    username = CustomTextField()
    password = CustomTextField()

    class Meta:
        table = "userdb"

