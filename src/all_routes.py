from fastapi import APIRouter
from src.routes import auth, products

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(products.router, prefix="/categories", tags=["products"])
