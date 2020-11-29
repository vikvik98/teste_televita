from flask import Flask
from flask_restful import Api
from department.views import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_db():
    db.create_all()

api = Api(app)
api.add_resource(DepartmentView, '/departments/')
api.add_resource(DepartmentDetailView, '/departments/<int:id>/')



if __name__ == '__main__':
    from dao.sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
