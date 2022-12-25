import bcrypt
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from datetime import datetime, timedelta
from src.schemas.user import CreateUser, UserLogin, RequestUserProfile, DeletetProfile
from src.models.user import User, UserProfile
from src.exceptions import ErrorResponseException
from src.app_settings import settings

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def validate_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    try:
        payload = jwt.decode(http_authorization_credentials.credentials, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
        if payload.get('exp') < int(datetime.now().timestamp()):
            raise HTTPException(status_code=403, detail="Token expired")
        return payload.get('username')
    except:
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )

async def create_user(user: CreateUser):
    check_email = await User.find_one({'email': user.email})
    if check_email:
        raise ErrorResponseException(data='email has been used')
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
    token = await generate_token(login.username)
    return {'token': token}


async def generate_token(username: str):
    expire = datetime.utcnow() + timedelta(seconds=60 * 60 * 24 * 3)
    to_encode = {"exp": expire, "username": username}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SECURITY_ALGORITHM)
    return encoded_jwt


async def create_profile(request: RequestUserProfile):
    check_email = await User.find_one({'email': request.email})
    if not check_email:
        raise ErrorResponseException(data='not found user')
    check_create_profile = await UserProfile.find_one({'email': request.email})
    if check_create_profile:
        raise ErrorResponseException(data='User profile already exists')
    create = UserProfile(**request.dict())
    await create.commit()
    return


async def get_profile():
    profile = await UserProfile.find().to_list(None)
    return [data.dump() for data in profile]


async def update_profile(request: RequestUserProfile):
    check_email = await UserProfile.find_one({'email': request.email})
    if not check_email:
        raise ErrorResponseException(data='not found user')
    check_email.update(request.dict())
    await check_email.commit()
    return check_email.dump()


async def delete_profile(request: DeletetProfile):
    check_email = await UserProfile.find_one({'email': request.email})
    if not check_email:
        raise ErrorResponseException(data='not found user')
    await check_email.delete()
    return