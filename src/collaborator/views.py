from collaborator.models import *
from flask_restful import Resource, reqparse

class CollaboratorView(Resource):
    args = reqparse.RequestParser()
    args.add_argument('id', type=int, required=True, help="The field 'id' cannot be left blank")
    args.add_argument('name')
    args.add_argument('department_id')

    def get(self):
        return {"collaborators": [collaborator.json() for collaborator in Collaborator.query.all()]}

    def post(self):
        data = CollaboratorView.args.parse_args()

        if Collaborator.find_collaborator(data['id']):
            return {"detail": "Collaborator id '{}' already exists".format(data['id'])}, 400

        collaborator = Collaborator(data['id'], data['name'], data['department_id'])
        collaborator.save_collaborator()
        return collaborator.json(), 201


class CollaboratorDetailView(CollaboratorView):
    def get(self, id):

        collaborator = Collaborator.find_collaborator(id)
        if collaborator:
            return collaborator.json()
        return {"detail": "Collaborator id '{}' not exists".format(id)}, 404

    def put(self, id):
        data = CollaboratorView.args.parse_args()
        collaborator = Collaborator.find_collaborator(id)
        if collaborator:
            collaborator.update_collaborator(data['name'], data['department_id'])
            collaborator.save_collaborator()
            return collaborator.json(), 200

        return {"detail": "Collaborator id '{}' not exists".format(id)}, 404

    def delete(self, id):
        collaborator = Collaborator.find_collaborator(id)
        if collaborator:
            collaborator.delete_collaborator()
            return {"detail": "Collaborator deleted"}, 204

        return {"detail": "Collaborator id '{}' not exists".format(id)}, 404


class CollaboratorDependentView(CollaboratorView):
    def get(self, id, dependent_id):

        collaborator = Collaborator.find_collaborator(id)
        if collaborator:
            if collaborator.add_dependents(dependent_id):
                collaborator.save_collaborator()
                return collaborator.json(), 200
            else:
                return {"detail": "Dependent id '{}' not exists".format(id)}, 404

        return {"detail": "Collaborator id '{}' not exists".format(id)}, 404

