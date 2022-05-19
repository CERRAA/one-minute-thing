from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    users = db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class User(db.Model, UserMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pass_secure = db.Column(db.String(200))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Posts', backref='poster', lazy='dynamic', passive_deletes=True)
    comments = db.relationship('Comment', backref='commenter', lazy='dynamic', passive_deletes=True)
    likes = db.relationship('Like', backref='liker', lazy='dynamic', passive_deletes=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

class Posts(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.Text)
    username = db.Column(db.String(255),index = True)
    category = db.Column(db.String(255),index =True)
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic', passive_deletes=True)
    likes = db.relationship('Like', backref='post', lazy='dynamic', passive_deletes=True)

    def save_p(self):
        db.session.add(self)
        db.session.commit()
    
       
    def __repr__(self):
        return f'Pitch {self.title}'


class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='CASCADE'))
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

class Like(db.Model):
    __tablename__='likes'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='CASCADE'))
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))