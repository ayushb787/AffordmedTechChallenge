from fastapi import APIRouter, HTTPException
from src.services.auth_service import get_auth_token

router = APIRouter()

@router.post("/")
def authenticate():
    try:
        token = get_auth_token()
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
