from auth.auth_controllers import router as authrouter
from fastapi import FastAPI

from db_pulse.configs.lifespans import master_lifespan

app = FastAPI(lifespan=master_lifespan)

app.include_router(authrouter)
