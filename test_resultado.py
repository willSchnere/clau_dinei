import pytest
import requests
from unittest.mock import MagicMock
from test_atividade import *

@pytest.fixture
def banco_mock(mocker):
    banco = BancoDeDados()
    mocker.patch.object(banco,'buscar_pedido', return_value={"id": 1,"Nome":"João"})
    return banco
def test_calcular_valor_total(mocker):
    mock_response = mocker.patch('resquests.get')  
    mock_response.return_value.json.return_value =[{"pedido":"pedido 1","preco":5.00,"quantidade":2},
                                                   {"pedido":"pedido 2","preco":10.00,"quantidade":10}]
    resultado = calcular_valor_total(1)
    assert  resultado ==   110                           
def test_obter_pedido_com_valor_total(mocker):
    mock_response = mocker.patch('resquests.get')
    mock_response.return_value.json.return_value={"id":1}
    resultado =  obter_pedido_com_valor_total(1)
    assert resultado == {"id":1,"Nome":"João","pedido":"pedido 1"}
    
    

    
 