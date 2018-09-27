orders = []

class Order:
    order_id = 1
    def __init__(self,name=None,description=None,price=None):
        self.id = Order.order_id
        self.name =  name
        self.description =  description
        self.price = price
        

        Order.order_id += 1


    def get_by_id(self, id):
        for order in orders:
            if order.id == id:
                return order
                

    def serialize(self):
        return dict (
            id = self.id,
            name = self.name,
            description = self.description,
            price=self.price
            )
