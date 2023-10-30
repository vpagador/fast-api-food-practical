import fastapi

router = fastapi.APIRouter()


@router.get('/menu/')
async def menu():
    return {'menu': ['pizza', 'pasta', 'salad', 'soup']}