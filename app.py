from fastapi import FastAPI, Form
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://0.0.0.0:8000","http://localhost.codechefvit.com","https://localhost.codechefvit.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# get method
@app.get("/")
async def root():
    return "Ok Working!"


# post method function
@app.post("/submit")
async def post_root(name: str = Form(...)):
    """To submit request"""
    return {"name": name}
