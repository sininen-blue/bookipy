from flask import Flask, render_template, request, redirect, url_for
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"


    final_chapter_content = []
    
    
    @app.get("/")
    def index_get():
        return render_template("index.html")
    
    
    @app.post("/process")
    def process():
        final_chapter_content.clear()
    
        chapter_url = request.form["chapter_url"]
    
        page = requests.get(chapter_url)
        soup = BeautifulSoup(page.content, "html.parser")
    
        chapter_content = soup.find(class_="chapter-content")
        chapter_content = soup.find_all("p")
    
        chapter_title = soup.find(class_="break-word").text
    
        final_chapter_content.append(f"<h1>{chapter_title}</h1>")
    
        for block in chapter_content:
            if block.text.isspace() is False:
                final_chapter_content.append(block)
    
        return redirect(url_for("page"))
    
    
    @app.get("/page")
    def page():
        return render_template("index.html", chapter_content=final_chapter_content)
    
    return app
