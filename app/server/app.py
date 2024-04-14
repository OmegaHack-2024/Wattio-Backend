from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.user import router as UserRouter
from server.routes.house import router as HouseRouter
from server.routes.house_log import router as HouseLogRouter
from server.routes.recommendation import router as RecommendationRouter
from server.routes.authentication import router as AuthRouter
from fastapi.staticfiles import StaticFiles
from decouple import config

is_production = config("PROJECT_ENVIRONMENT", default="DEVELOPMENT")

if is_production == "RELEASE":
    app = FastAPI(
        docs_url=None,  # Disable docs (Swagger UI)
        redoc_url=None,  # Disable redoc
    )
else:
    app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthRouter, tags=["Authentication"])
app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(HouseRouter, tags=["House"], prefix="/house")
app.include_router(HouseLogRouter, tags=["HouseLog"], prefix="/house_log")
app.include_router(
    RecommendationRouter, tags=["Recommendation"], prefix="/recommendation"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Wattio!"}
