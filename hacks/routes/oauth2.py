from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from datetime import datetime, timedelta
from .. import schemas
from fastapi.security import OAuth2PasswordBearer

# secret key
# Algorithm HS256
# Experation time

Oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099fsf0f4caa6cf63788e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credential_exceptions):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credential_exceptions

        token_data = schemas.Token_data(id=id)
    except JWTError:
        raise credential_exceptions

    return token_data


def get_current_user(token: str = Depends(Oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                          detail=f"Could not valdidate credential",
                                          headers={"www-Authenticate": "Bearer"})
    return verify_access_token(token,credentials_exception)
