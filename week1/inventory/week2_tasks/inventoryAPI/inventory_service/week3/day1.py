from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# 1. సెక్యూరిటీ కాన్ఫిగరేషన్ (రియల్ టైమ్‌లో ఇవి .env ఫైల్‌లో ఉండాలి)
SECRET_KEY = "SUPER_SECRET_KEY_DONT_SHARE_THIS"  # మీ రహస్య కీ
ALGORITHM = "HS256"                              # వాడే అల్గారిథమ్
ACCESS_TOKEN_EXPIRE_MINUTES = 15                 # టోకెన్ వాలిడిటీ టైమ్

# పాస్‌వర్డ్ హ్యాషింగ్ కోసం (BCrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# టోకెన్ ఎక్కడి నుండి తీసుకోవాలో చెప్పే FastAPI టూల్
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# డెమో కోసం ఒక నకిలీ డేటాబేస్ (Fake Database)
# ఇక్కడ పాస్‌వర్డ్ "secret123" ను హ్యాష్ చేసి దాచాము
fake_users_db = {
    "kiran": {
        "username": "kiran",
        "full_name": "Kiran Kumar",
        "email": "kiran@example.com",
        "hashed_password": pwd_context.hash("secret123"), 
    }
}

# Pydantic మోడల్ (రెస్పాన్స్ ఫార్మాట్ కోసం)
class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None

# (Helper Functions)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="టోకెన్ చెల్లాబాటదు లేదా యూజర్ ఎవరో తెలియదు",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # టోకెన్‌ను డీకోడ్ చేస్తున్నాం
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
        
    user = fake_users_db.get(username)
    if user  is None:
        raise credentials_exception
    return User(**user)


# --- API ఎండ్‌పాయింట్లు (API Endpoints) ---

# 1. లాగిన్ API (టోకెన్ జనరేట్ చేస్తుంది)
@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="యూజర్ నేమ్ లేదా పాస్‌వర్డ్ తప్పు",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # లాగిన్ సక్సెస్ అయితే టోకెన్ క్రియేట్ చేస్తాం
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# 2. ప్రొటెక్టెడ్ API (ఈ డేటా చూడాలంటే కచ్చితంగా JWT టోకెన్ ఉండాలి)
@app.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
