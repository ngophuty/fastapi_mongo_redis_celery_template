import bcrypt
from src.schemas.user import CreateUser, UserLogin
from src.models.user import User
from src.exceptions import ErrorResponseException


async def create_user(user: CreateUser):
    check_user = await User.find_one({'username': user.username})
    if check_user:
        raise ErrorResponseException(data='User already exists')
    create = User(
        email=user.email,
        username=user.username,
        password= hash_password(user.password)
     )
    await create.commit()
    return

def hash_password(password: str):
    encode_pass = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    pwd_hash = bcrypt.hashpw(encode_pass, mySalt)
    return pwd_hash.decode('utf-8')


async def user_login(login: UserLogin):
    encode_pass = login.password.encode('utf-8')
    check_user = await User.find_one({'username': login.username})
    if not check_user:
        raise ErrorResponseException(data='Wrong username or password !')
    get_password = check_user.dump().get('password')
    check_pass= get_password.encode('utf-8')
    result = bcrypt.checkpw(encode_pass, check_pass)
    if not result: 
        raise ErrorResponseException(data='Wrong username or password !')
    return {'message': "login success"}