from fastapi import FastAPI

from db_pulse.configs.lifespans import master_lifespan

from .auth.auth_controllers import router as authrouter

app = FastAPI(lifespan=master_lifespan)

app.include_router(authrouter)
