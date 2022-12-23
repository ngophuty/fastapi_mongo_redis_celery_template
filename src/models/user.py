from umongo import Document, fields
from src.database.connect_mongodb import umongo_cnx


@umongo_cnx.register
class User(Document):
    user_name = fields.StrField(allow_none=True)
    pass_word = fields.StrField(allow_none=True)