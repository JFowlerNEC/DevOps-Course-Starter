from todo_app.flask_config import Config

from flask import Flask, render_template, request, redirect
from todo_app.data import trello_items as trello


app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    todo_items = trello.get_items()
    return render_template ('index.html',items=todo_items)

@app.route('/add', methods=['POST'])
def add_item():
    title = request.form.get('title')
    status = request.form.get('status')
    trello.add_item(title,status)
    return redirect
