from umongo import Document, fields
from src.database.connect_mongodb import umongo_cnx


@umongo_cnx.register
class User(Document):
    username = fields.StrField(allow_none=True)
    password = fields.StrField(allow_none=True)
    email = fields.StrField(allow_none=True)


@umongo_cnx.register
class UserProfile(Document):
    full_name = fields.StrField(allow_none=True)
    phone_number = fields.StrField(allow_none=True)
    email = fields.StrField(allow_none=True)
    address = fields.StrField(allow_none=True)