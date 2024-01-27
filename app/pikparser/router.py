from fastapi import APIRouter
from app.pikparser.pik import get_data_from_pik_api

router = APIRouter(prefix="/pik")

@router.get('/get_data')
def get_data_from_pik_api_endpoint():
        return get_data_from_pik_api()