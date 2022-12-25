from umongo import Document, fields
from src.database.connect_mongodb import umongo_cnx


@umongo_cnx.register
class User(Document):
    username = fields.StrField(allow_none=True)
    password = fields.StrField(allow_none=True)
    email = fields.StrField(allow_none=True)