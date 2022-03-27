"""
Flask Service Sample Blueprint
"""

from flask import Blueprint, abort
from flask.json import jsonify
from flask_jwt_extended import jwt_required


blueprint = Blueprint("todo", __name__)

todos = [
    {"summary": "Pick up groceries", "status": "TO-DO"},
    {"summary": "Take out trash", "status": "TO-DO"},
    {"summary": "Do laundry", "status": "DONE"},
    {"summary": "Give dog a bath", "status": "TO-DO"},
]


@blueprint.route("/api/todos", methods=["GET"])
@jwt_required()
def list_todos():
    """
    List all
    """
    return jsonify(todos)


@blueprint.route("/api/todos/<int:todo_id>", methods=["GET"])
@jwt_required()
def get_todo(todo_id):
    """
    Get item
    """
    if todo_id < len(todos):
        return jsonify(todos[todo_id])
    else:
        abort(400, "Invalid ID")
