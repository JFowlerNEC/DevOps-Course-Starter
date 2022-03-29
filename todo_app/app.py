
from flask import Flask, render_template, request, redirect
from todo_app.data import session_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    todo_items = session_items.get_items()
    return render_template ('index.html',items=todo_items)

@app.route('/add', methods=['POST'])
def add_item():
    title = request.form.get('title')
    status = request.form.get('status')
    todo_items = session_items.add_item(title,status)
    return redirect('/')
