from flask import Flask
from RPS.routes import RPS
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'c7e5fb3c42586286931c3e6f348a8709356b1015c8c4cd32b575316db902'
    app.register_blueprint(RPS)
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
