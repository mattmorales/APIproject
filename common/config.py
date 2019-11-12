from api import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = "NoPasswordIsSafe"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['BASIC_AUTH_USERNAME'] = 'txstate'
app.config['BASIC_AUTH_PASSWORD'] = 'txstate'
app.config['BASIC_AUTH_FORCE'] = True