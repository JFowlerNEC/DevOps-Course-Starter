from todo_app.flask_config import Config

from flask import Flask, render_template, request, redirect
from todo_app.data import trello_items as trello


app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    todo_items = trello.get_todo_items()
    doing_items = trello.get_doing_items()
    done_items = trello.get_done_items()
    return render_template ('index.html',items=todo_items,items_doing=doing_items,items_done=done_items)

@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    trello.add_item(title)
    return redirect(url_for('index'))

@app.route('/items/<id>/complete')
def complete_item(id):
    session.complete_item(id)
    trello.complete_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/todo')
def todo_item(id):
    trello.start_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/doing')
def doing_item(id):
    trello.progress_item(id)
    return redirect(url_for('index'))   