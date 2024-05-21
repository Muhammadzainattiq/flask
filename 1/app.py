from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()
with app.app_context():
    db.create_all()
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def hello_world():
    todo = Todo(title = "First Todo", desc = "Start investing in Stock market")
    db.session.add(todo)
    db.session.commit()
    secondtodo = Todo(title = "Second Todo", desc = "Start drinking water after again and again")
    db.session.add(secondtodo)
    db.session.commit()
    return render_template('index.html')
@app.route('/products')
def products():
    return 'this is the products page'

if __name__ == "__main__":
    app.run(debug=True, port=8000)