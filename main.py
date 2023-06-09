from fastapi import FastAPI, Request
import logging
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    logging.debug(Request().headers)
    return "Hello Vidura."


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
