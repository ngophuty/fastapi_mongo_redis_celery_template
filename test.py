import jwt
from datetime import datetime, timedelta

def generate_token(username: str):
    expire = datetime.utcnow() + timedelta(seconds=60 * 60 * 24 * 3)
    to_encode = {"exp": expire, "username": username}
    encoded_jwt = jwt.encode(to_encode, 'tynp', algorithm='HS256')
    return encoded_jwt

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzIyNDA3NzMsInVzZXJuYW1lIjoidHlucCJ9.xD-XoR9IBeitF6bZ6Nc_ADwC8Eu_iLvfwXlwOAtASW8'

de = jwt.decode(token, key='tynp@1234', algorithms=['HS256'])

a =datetime.now().timestamp()
print(a)