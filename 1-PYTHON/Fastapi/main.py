import uvicorn # ASGI
from fastapi import FastAPI

app = FastAPI()


# it follws asgi interface = asyncronous server gateway interface


# get index route ('/'), opens automatically in http server

@app.get('/')
def index():
    return {'message':'Hello, mohit'}


# to route with a single parameters
@app.get('/welcome')
def get_name(name: str):
    return{'welcome to mohit page':f'{name}'}


# run the api using uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)

# command to run - uvicorn main:app --reload