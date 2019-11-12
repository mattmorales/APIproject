from api import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from api.movies import Movie, Genre, Actor
from api.accounts import User, Role


#Flask Admin
admin = Admin(app, name='movielog', template_mode='bootstrap3')
admin.add_view(ModelView(Movie, db.session))
admin.add_view(ModelView(Genre, db.session))
admin.add_view(ModelView(Actor, db.session))
admin.add_view(ModelView(User, db.session))
# Add model views
admin.add_view(ModelView(Role, db.session))

