from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime

class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
