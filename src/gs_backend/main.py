import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from gs_backend.schemas import Message

app = FastAPI()
current_dir = os.path.dirname(__file__)
static_dir = os.path.join(current_dir, "../static_files")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")


@app.get('/api', status_code=200, response_model=Message)
def read_api_root():
    return {'message': 'api root'}
