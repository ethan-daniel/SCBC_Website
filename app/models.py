from app import db


class MarkerRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    latitude = db.Column(db.Float(64), index=True)
    longitude = db.Column(db.Float(64), index=True)
    description = db.Column(db.String(120), index=True)
    type = db.Column(db.String(15), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def get_all():
        return MarkerRequest.query.all()
