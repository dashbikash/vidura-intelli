from fastapi import FastAPI, Request
import logging
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    logging.debug(Request.headers)
    return "Hello Vidura"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
