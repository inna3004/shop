import requests
from flowers.models import OrderItem, Flower


class WarehouseClient:
    def __init__(self):
        self.base_url = 'http://localhost:9000'

    def check_flower_availability(self, flower: Flower):
        response = requests.get(f"{self.base_url}/check/{flower.id}")
        if response.status_code != 200:
            return False
        data = response.json()
        return data['available']

    def start_assemble(self, order: OrderItem):
        response = requests.post(f"{self.base_url}/assemble", json={
            'external_id': order.flower.id,
            'quantity': order.quantity,
        })
        if response.status_code != 200:
            return False
        return True





