import requests
from .schema import SPik 
from .settings import headers

def get_data_from_pik_api():
    response = requests.get(
            'https://flat.pik-service.ru/api/v1/filter/flat-by-block/320?type=1,2&location=2,3&currentBenefit=polnaya-oplata&rooms=3&areaFrom=75&areaTo=83&floorFrom=3&floorTo=18&flatPage=2&flatLimit=8&onlyFlats=1',
            headers=headers,
    ).json()
    spik = SPik(**response)

    return spik.model_dump()