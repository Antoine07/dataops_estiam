# pylint: skip-file 

from src.data_manager import Data_Manager

def test_addition():
    assert 2 + 2 == 4
    
def test_data_manager():
    sample_data = [
        {"order_id": 1, "amount": 150.0},
        {"order_id": 2, "amount": 200.0},
        {"order_id": 3, "amount": 50.0},
    ]
    manager = Data_Manager(sample_data)
    assert manager.get_orders() == sample_data
    assert manager.total_sales() == 400.0   