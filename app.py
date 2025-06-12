# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fastapi",
# ]
# ///
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
