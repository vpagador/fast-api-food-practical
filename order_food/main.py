import fastapi
import uvicorn
import restaurant.order
import restaurant.menu

api = fastapi.FastAPI()

def configure_routing():
    api.include_router(restaurant.menu.router)
    api.include_router(restaurant.order.router)

if __name__ == '__main__':
    configure_routing()
    uvicorn.run(api, port=8000, host='127.0.0.1')