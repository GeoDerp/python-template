import os.path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()


def get_html_response() -> str:
    file: str = "src/python_template/templates/hello.html"
    if os.path.isfile(file):
        with open(file) as f:
            return f.read()
    else:
        raise HTTPException(status_code=404, detail="HTML template not found")


@app.get("/", response_class=HTMLResponse)
async def root():
    return get_html_response()


# if running with uvicorn
def main():
    uvicorn.run("python_template.main:app", host="0.0.0.0", port=8080, reload=True)
