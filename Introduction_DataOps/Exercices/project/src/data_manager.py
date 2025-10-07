
class Data_Manager:
    def __init__(self, data: list[dict]):
        self.data = data
        
    def get_orders(self) -> list[dict]:
        return self.data
    
    def total_sales(self) -> float:
        return sum(order["amount"] for order in self.data)

    def average_order_value(self) -> float:
        if not self.data:
            return 0.0
        return self.total_sales() / len(self.data)

    def best_order(self) -> dict | None:
        if not self.data:
            return None
        return max(self.data, key=lambda order: order["amount"])