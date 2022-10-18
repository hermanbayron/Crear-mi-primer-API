import json
import flask
from flask import request
from flask import jsonify
from flask import Flask
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    # puedes convertir una variable en un string json así
    json_text = flask.jsonify(todos)
    # y luego puedes retornarla (return) en el response body así:
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # request.get_json(force=True)
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return flask.jsonify(todos)
    # 'Response for the POST todo'

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    print("This is the position to delete: ",position)
    return jsonify(todos)

    # The request DELETE /todos/1 will call the function `delete_todo` with the variable position == 1
    # The request DELETE /todos/323 will call the function `delete_todo` with the variable position == 323

# Estas dos líneas siempre seben estar al final de tu archivo app.py.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)