from .base import db
from datetime import datetime


class System(db.Model):
     """
      Create an System table
      """

     __tablename__ = 'system'

     id = db.Column(db.Integer, primary_key=True)
     version_no = db.Column(db.Float, nullable=False)
     secret_key = db.Column(db.String(255),unique=True)
     expiry_date = db.Column(db.DateTime, nullable=False)
     created_at = db.Column(db.DateTime, default=datetime.now())
     updated_at = db.Column(db.DateTime, default=datetime.now())
     deleted_at = False
     def __repr__(self):
        return '<System: {}>'.format(self.version_no)