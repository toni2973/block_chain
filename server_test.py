from flask import Flask, request
from flask.ext.restful import reqparse, abort, Api, Resource
from produce import produce
from process import process
from transport import transport
from bigchaindb_driver.crypto import CryptoKeypair
import json
import requests

app = Flask(__name__)
api = Api(app)

TODOS = {
    'produce': {'task': 'build an API'},
    'process': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class keyPair:
    def __init__(self,verifying_key,signing_key):
        self.verifying_key=verifying_key
        self.signing_key=signing_key

# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    # def get(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     return TODOS[todo_id]

    # def delete(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     del TODOS[todo_id]
    #     return '', 204
    #
    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201

    def post(self, todo_id):
        # args = parser.parse_args()
        # print(request.get_data())
        args = request.get_json(force=True)
        # print(args)
        owner=keyPair(signing_key=args.get('owner')[0],verifying_key=args.get('owner')[1])
        # print(owner.verifying_key+" "+" "+owner.signing_key)
        switch = {
            'produce': lambda args: produce(owner=owner, name=args.get('name'), size=args.get('size'),
                                            util=args['util'], place=args['place'],
                                            manufacturer=args['manufacturer'], detail=args['detail'],
                                            amount=args['amount']),
            'process': lambda args: process(materials=args['materials'], recovery=args['recovery'], owner=args['owner'],
                                            name=args['name'], size=args['size'], unit=args['unit'],
                                            place=args['place'],
                                            manufacturer=args['manufacturer'], amount=args['amount']
                                            ),
            'transport': lambda args: transport(owner_before=args['owner_before'], owner_after=args['owner_after'],
                                                goods_id=args['goods_id'], amount=args['amount'])
        }[todo_id](args)
        return switch, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


##
## Actually setup the Api resource routing here
##
# api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/task/<todo_id>')

app.run('localhost', '5020')
