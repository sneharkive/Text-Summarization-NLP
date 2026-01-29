# from fastapi import FastAPI
# import uvicorn
# import sys
# import os
# from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
# from fastapi.responses import Response
# from textSummarizer.pipeline.prediction import PredictionPipeline
#
# text: str = "What is Text Summarization?"
#
# app = FastAPI()
#
#
# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")
#
#
# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return Response("Training successful !!")
#
#     except Exception as e:
#         return Response(f"Error Occurred! {e}")
#
#
# @app.post("/predict")
# async def predict_route(text):
#     try:
#
#         obj = PredictionPipeline()
#         text = obj.predict(text)
#         return text
#     except Exception as e:
#         raise e
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080)


from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI(title="Text Summarization App")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "summary": None}
    )


@app.post("/", response_class=HTMLResponse)
async def summarize(request: Request, text: str = Form(...)):
    obj = PredictionPipeline()
    summary = obj.predict(text)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "summary": summary}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)



# to run it use the following command
# uvicorn app:app --reload