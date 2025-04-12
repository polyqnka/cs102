import pytest
from src.lab5.orders_validator import validate_and_process_orders

class TestValidateAndProcessOrders:
    def test_valid(self):
        orders = [
            "1;apple, banana;John Doe;Country. Region. City. Street;+1-123-456-78-90;MAX",
            "2;orange;Jane Doe;Country. Region. City. Avenue;+1-987-654-32-10;MIDDLE"
        ]
        expected_valid = [
            "1;apple, banana;John Doe;Region. City. Street;+1-123-456-78-90;MAX",
            "2;orange;Jane Doe;Region. City. Avenue;+1-987-654-32-10;MIDDLE"
        ]
        expected_invalid = []

        valid_orders, invalid_orders = validate_and_process_orders(orders)

        assert valid_orders == expected_valid
        assert invalid_orders == expected_invalid

    def test_invalid_address(self):
        orders = [
            "1;apple, banana;John Doe;InvalidAddress;+1-123-456-78-90;MAX"
        ]
        expected_valid = []
        expected_invalid = ["1;1;InvalidAddress"]

        valid_orders, invalid_orders = validate_and_process_orders(orders)

        assert valid_orders == expected_valid
        assert invalid_orders == expected_invalid

    def test_invalid_phone(self):
        orders = [
            "1;apple, banana;John Doe;Country. Region. City. Street;12345;MAX"
        ]
        expected_valid = []
        expected_invalid = ["1;2;12345"]

        valid_orders, invalid_orders = validate_and_process_orders(orders)

        assert valid_orders == expected_valid
        assert invalid_orders == expected_invalid

    def test_mixed(self):
        orders = [
            "1;apple, banana;John Doe;Country. Region. City. Street;+1-123-456-78-90;MAX",
            "2;orange;Jane Doe;InvalidAddress;+1-987-654-32-10;MIDDLE",
            "3;grape;Jake Doe;Country. Region. City. Avenue;invalidphone;LOW"
        ]
        expected_valid = [
            "1;apple, banana;John Doe;Region. City. Street;+1-123-456-78-90;MAX"
        ]
        expected_invalid = [
            "2;1;InvalidAddress",
            "3;2;invalidphone"
        ]

        valid_orders, invalid_orders = validate_and_process_orders(orders)

        assert valid_orders == expected_valid
        assert invalid_orders == expected_invalid

    def test_duplicate_products(self):
        orders = [
            "1;apple, banana, apple;John Doe;Country. Region. City. Street;+1-123-456-78-90;MAX"
        ]
        expected_valid = [
            "1;apple x2, banana;John Doe;Region. City. Street;+1-123-456-78-90;MAX"
        ]
        expected_invalid = []

        valid_orders, invalid_orders = validate_and_process_orders(orders)

        assert valid_orders == expected_valid
        assert invalid_orders == expected_invalid
