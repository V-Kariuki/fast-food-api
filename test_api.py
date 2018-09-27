import unittest

import json

from app import create_app

from unittest import TestCase

from flask_restful import Resource

from app.api.v1.views import Specific_Order, Orders




class TestApi(unittest.TestCase):

    

    def setUp(self):

        self.app = create_app("testing")

        self.client = self.app.test_client()

        self.app_context = self.app.app_context()

        self.new_order = {"name": "Kuku", "price": 2000, "description": "tamu"}



    def test_get_orders(self):
        """
            Tests if the route gets a list of all orders
    """
        response = self.client.get('/api/v1/orders' ,content_type='application/json')
        self.assertEqual(response.status_code, 200)



    def test_post_orders(self):

        response = self.client.post('/api/v1/orders', data = json.dumps(self.new_order), content_type='application/json')

        self.assertEqual(response.status_code, 201)

    
    def test_one_order(self):
        """Returns a 200 status code if an order is fetched"""
        response = self.client.get('/api/v1/orders/1' ,content_type='application/json')

        self.assertEqual(response.status_code, 200)


    def test_put_order(self):

        response = self.client.put('/api/v1/orders/1', data = json.dumps(self.new_order), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_delete_order(self):
        res = self.client.delete('/api/v1/orders/1', content_type='application/json')
        self.assertEqual(res.status_code, 204)



if __name__ == '__main__':

    unittest.main()
