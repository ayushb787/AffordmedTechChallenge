from fastapi import APIRouter
from src.routes.auth import router as auth_router
from src.routes.products import router as products_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(products_router, prefix="/categories", tags=["products"])
