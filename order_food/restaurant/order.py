import fastapi

router = fastapi.APIRouter()


@router.post('/order/')
async def order(item: str, quantity: int): 
    print(f'Order received for {quantity} of {item}')