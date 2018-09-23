from flask import Flask
from flask_restful import Api
from app.api.v1.views import Orders, Specific_Order
from instance.config import app_config


def create_app(config_name='development'):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config["development"])
	app.config.from_pyfile('config.py')
	from .api.v1 import orders_bp as orders_blueprint
	api = Api(orders_blueprint)
	app.register_blueprint(orders_blueprint, url_prefix='/api/v1')
	api.add_resource(Orders, '/orders')
	api.add_resource(Specific_Order, '/orders/<int:id>')

	return app
	
