from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("index.html")


@app.post("/")
def index_post():
    chapter_url = request.form["chapter_url"]
    final_chapter_content = []

    page = requests.get(chapter_url)
    soup = BeautifulSoup(page.content, "html.parser")

    chapter_content = soup.find(class_="chapter-content")
    chapter_content = soup.find_all("p")

    for block in chapter_content:
        if block.text.isspace() is False:
            # remove the text from the span and put it into a block
            final_chapter_content.append(block)

    return render_template("index.html", chapter_content=final_chapter_content)
