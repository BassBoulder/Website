from flask improt Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abc123'

    return app