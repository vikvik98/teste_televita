from dao.sql_alchemy import db


class Collaborator(db.Model):
    __tablename__ = "collaborators"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(200))
    have_dependents = db.Column(db.Boolean)
    department_id = db.Column(db.INTEGER, db.ForeignKey('departments.id'))
    dependent_id = db.Column(db.INTEGER, db.ForeignKey("collaborators.id"))
    dependents = db.relationship('Collaborator', remote_side=[id], uselist=True)

    def __init__(self, id, name, department_id):
        self.id = id
        self.name = name
        self.department_id = department_id

    def json(self):
        if self.have_dependents:
            return {
                "id": self.id,
                "name": self.name,
                "department_id": self.department_id,
                "have_dependets": self.have_dependents
            }

        return {
            "id": self.id,
            "name": self.name,
            "department_id": self.department_id
        }


    @classmethod
    def find_collaborator(cls, id):
        collaborator = cls.query.filter_by(id=id).first()
        if collaborator:
            return collaborator
        return None

    def save_collaborator(self):
        db.session.add(self)
        db.session.commit()

    def update_collaborator(self, name, department_id):
        self.name = name
        self.department_id = department_id

    def delete_collaborator(self):
        db.session.delete(self)
        db.session.commit()


    def add_dependents(self, dependent_id):
        collaborator = Collaborator.query.filter_by(id=dependent_id).first()
        if collaborator:
            if self.dependent_id:
                self.dependents.append(collaborator)
            else:
                self.dependent_id = dependent_id
            self.have_dependents = True
            return collaborator

        return None