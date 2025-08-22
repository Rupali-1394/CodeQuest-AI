from urllib.request import Request
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge
import os
from clerk_backend_api import Clerk


clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

app.include_router(challenge.router, prefix="/api")