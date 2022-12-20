from typing import List, Optional, Union

from pydantic import BaseSettings


class MongoDBSettings(BaseSettings):

   MONGODB_HOST: str
   MONGODB_PORT: Union[int,str]
   MONGODB_USERNAME: str
   MONGODB_PASSWORD: str
   MONGODB_NAME: str
