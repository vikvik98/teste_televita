from dao.sql_alchemy import db


class Department(db.Model):
    __tablename__ = "department"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(200))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def find_department(cls, id):
        department = cls.query.filter_by(id=id).first()
        if department:
            return department
        return None

    def save_department(self):
        db.session.add(self)
        db.session.commit()

    def update_department(self, name):
        self.name = name

    def delete_department(self):
        db.session.delete(self)
        db.session.commit()