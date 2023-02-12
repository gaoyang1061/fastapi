from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get('/')
def getSample():
    return JSONResponse({"result": "hello world"})

@app.post('/')
async def predict(file: UploadFile = File(...)):

    return JSONResponse({"Post": "hello from Post"})


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9000)
