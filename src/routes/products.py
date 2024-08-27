from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from src.services.product_service import fetch_products, fetch_product_details
from src.schemas.product import ProductResponse

router = APIRouter()

@router.get("/{categoryname}/products", response_model=List[ProductResponse])
def get_products(
    categoryname: str,
    n: int = Query(10, gt=0),
    minPrice: int = Query(1),
    maxPrice: int = Query(10000),
    company: Optional[str] = Query(None, regex="^(AMZ|FLP|SNP|PIYN|AZO)$"),
    page: int = Query(1, gt=0),
    sort_by: Optional[str] = Query(None, regex="^(rating|price|company|discount)$"),
    order: Optional[str] = Query("asc", regex="^(asc|desc)$")
):
    try:
        products = fetch_products(categoryname, n, minPrice, maxPrice, company, page, sort_by, order)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
#
# @router.get("/{categoryname}/products/{productid}", response_model=ProductResponse)
# def get_product_details(categoryname: str, productid: str, company: str):
#     try:
#         product = fetch_product_details(categoryname, productid, company)
#         return product
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))
