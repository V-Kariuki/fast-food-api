from flask_restful import Resource
from flask import  Flask,jsonify,request,Response
from app.models import orders, Order


orders = []

class Orders(Resource):
    """
    GET/ all orders placed
    POST/ a new order
    """
    
    def get(self):
        """Return a list of all orders posted"""
        if len(orders) == 0:
            return {'messsage': 'No orders currently'}, 200
        return {'orders': orders}, 200

    def post(self):
        """Posts a specific order"""
        order_data = {}
        data = request.get_json(force = True)
        order_data['name'] = data['name']
        order_data['price'] = data['price']
        order_data['description'] = data['description']
        order_data['status'] = data['status']
        order_data['id'] = len(orders) + 1    
        orders.append(order_data)
        if not data['name'] or not data['price'] or not data['description']:
            return {'message':'Please enter your order information'}
        elif type(data['name']) != str and type(data['price']) != int and type(data['description']) != str :
            return {'message':'You have entered incorrect data types'}
        elif type(data['name']) != str or type(data['description']) != str:
            return {'message':'Expected a string'}
        elif not isinstance (data['price'],int):
            return {'message':'You have entered incorrect data type for the price'}
        else:
            return {'orders': order_data}, 201

class Specific_Order(Resource):
    """
    GET/ a specific order
    PUT/ edit a specific order
    DELETE/ delete a specific order 
    """
    def get(self, id):
        order = [order for order in orders if order['id'] == id]
        if order:
            return {'order': order[0]}, 200
        else:
            return {'message':'Error,your order was not found'}, 200
    
    def put(self, id):
        order = [order for order in orders if order['id'] == id]
        if order:
            data = request.get_json(force = True)
            order[0]['name'] = data['name']
            order[0]['price'] = data['price']
            order[0]['description'] = data['description']
            order[0]['status']  = data['status']
            # orders.append(order_data)
            return {'order': order[0]}, 200
        else:
            return {'message':'Error ,Invalid order'}, 200
    
    def delete(self, id):
        order = [order for order in orders if order['id'] == id]
        if order:
            del orders[0]
            return {'orders': orders}, 204
        else:
            return {'message': 'Error ,Invalid order'}, 204
