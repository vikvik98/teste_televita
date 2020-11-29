from department.models import *
from flask_restful import Resource, reqparse

class DepartmentView(Resource):

    args = reqparse.RequestParser()
    args.add_argument('id')
    args.add_argument('name')

    def get(self):

        return {"departmets": [department.json() for department in Department.query.all()]}


    def post(self):

        data = DepartmentView.args.parse_args()

        if Department.find_department(data['id']):
            return {"detail": "Department id '{}' already exists".format(data['id'])}, 400

        departament = Department(data['id'], data['name'])
        departament.save_department()
        return departament.json(), 201


class DepartmentDetailView(DepartmentView):

    def get(self, id):

        departament = Department.find_department(id)
        if departament:
            return departament.json()
        return {"detail": "Department id '{}' not exists".format(id)}, 404

    def put(self, id):
        data = DepartmentView.args.parse_args()
        departament = Department.find_department(id)
        if departament:
            departament.update_department(data['name'])
            departament.save_department()
            return departament.json(), 200

        return {"detail": "Department id '{}' not exists".format(id)}, 404

    def delete(self, id):
        departament = Department.find_department(id)
        if departament:
            departament.delete_department()
            return {"detail": "Department deleted"}, 204

        return {"detail": "Department id '{}' not exists".format(id)}, 404



