from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.user import router as UserRouter
from server.routes.vehicle import router as VehicleRouter
from server.routes.house import router as HouseRouter
from server.routes.recommendation import router as RecommendationRouter
from server.routes.redeemable import router as RedeemableRouter
from server.routes.redemption_history import router as RedemptionHistoryRouter
from server.routes.user_points_transaction import router as UserPointsTransactionRouter
from server.routes.ride import router as RideRouter
from server.routes.authentication import router as AuthRouter
from fastapi.staticfiles import StaticFiles
from decouple import config

is_production = config('PROJECT_ENVIRONMENT', default="DEVELOPMENT")

if is_production == 'RELEASE':
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
app.include_router(RecommendationRouter, tags=[
                   "Recommendation"], prefix="/recommendation")

app.include_router(VehicleRouter, tags=["Vehicle"], prefix="/vehicle")
app.include_router(RedeemableRouter, tags=["Redeemable"], prefix="/redeemable")
app.include_router(RedemptionHistoryRouter, tags=[
                   "RedemptionHistory"], prefix="/redemption_history")
app.include_router(UserPointsTransactionRouter, tags=[
                   "UserPointsTransaction"], prefix="/user_points_transaction")
app.include_router(RideRouter, tags=["Ride"], prefix="/ride")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Wattio!"}
