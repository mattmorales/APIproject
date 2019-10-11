from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['FLASK_ADMIN_SWATCH'] = 'Cerulean'
db = SQLAlchemy(app)


class Movies(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable = False)

    def __repr__(self):
        return '<Title %r>' % self.title


class MoviesView(ModelView):
     can_delete = False

db.create_all()

admin = Admin(app, name = 'movielog', template_mode = 'bootstrap3')
admin.add_view(ModelView(Movies, db.session))

if __name__=='__main__':
    app.run(debug=True)