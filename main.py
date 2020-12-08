from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/predict', response_class=HTMLResponse)
async def predict(request: Request, title: str = Form(...)):
    #load model 
    model_filename = "./model/news_title.joblib"
    clf = joblib.load(model_filename)
    # Receives the input query from form
    data = [title]
    probas = clf.predict_proba([str(data)])[0]
    predict = clf.predict(data)
    classes = clf.classes_

    return templates.TemplateResponse("result.html", {"request": request, "probas":probas, "predict":predict, "classes": classes})