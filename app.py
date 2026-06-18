from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Task

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json

    task = Task(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'Pending')
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict())

# Get All Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Update Task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"message":"Task not found"}),404

    data = request.json

    task.title = data['title']
    task.description = data['description']
    task.status = data['status']

    db.session.commit()

    return jsonify(task.to_dict())

# Delete Task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"message":"Task not found"}),404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message":"Task Deleted"})

if __name__ == '__main__':
    app.run(debug=True)