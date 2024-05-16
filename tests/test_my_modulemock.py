import pytest 
from source.my_modulemock import f1, f2, fetch_product_price, calculate_tax
from unittest.mock import patch


def test_f2_with_fixed_f1():
    with patch('source.my_modulemock.f1', return_value=5) as mock_f1 :
        assert f2() == 50
        mock_f1.assert_called_once()

def test_calculate_tax_with_fixed_product_price():
    with patch('source.my_modulemock.fetch_product_price', return_value=2) as mock_product_price :
        assert calculate_tax(1) == 0.40
        mock_product_price.assert_called_once_with(1)

@pytest.mark.parametrize("price, expected_price",
                          [(2, 0.40), (4,0.80)])
def test_multiple_price(price, expected_price):
    with patch('source.my_modulemock.fetch_product_price', return_value=price) as mock_product_price :
        assert calculate_tax(1) == expected_price
        mock_product_price.assert_called_once_with(1)