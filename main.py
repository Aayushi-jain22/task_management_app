from src.utils.settings import settings
from src.utils.db import Base, engine
from fastapi import FastAPI



Base.metadata.create_all(engine)
app = FastAPI(title="Task Management API", description="API for managing tasks", version="1.0.0")