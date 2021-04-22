from flask import Flask
from  .extensions import mongo
from .views import bp

def create_app(config_object="bookproject.settings"):
    app = Flask(__name__)

    app.config.from_object(config_object)
    
    mongo.init_app(app)
    
    app.register_blueprint(bp)
    return app

from bookproject import views
if __name__ == "__main__":
    app.run(debug=True)