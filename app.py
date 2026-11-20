# SPDX-FileCopyrightText: 2026 Pardha Saradhi Edupalli
# SPDX-License-Identifier: MIT

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/assignment/', methods=['POST', 'GET'])
def assignment():
    if request.method == 'POST':
        content = request.form.get('content', '').strip()
        if not 1 <= len(content) <= 200:
            return render_template('index.html', tasks=Todo.query.order_by(Todo.id).all(),
                                   error='Enter a task between 1 and 200 characters.'), 400
        new_task = Todo(content=content)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('assignment'))
    tasks = Todo.query.order_by(Todo.id).all()
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
