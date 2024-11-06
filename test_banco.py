import pytest
import requests
from unittest.mock import MagicMock

class BancoDeDados:
    def buscar_usuario(self,user_id):
        raise NotImplementedError
    
def obter_dados_adicionais(user_id):
    resposta = requests.get(f"http://api.exemplo.com/dados/{user_id}")
    return resposta.json()

def sistema_principal(user_id,banco):
    usuario = banco.buscar_usuario(user_id)
    dados_adicionais = obter_dados_adicionais(user_id)
    usuario.update(dados_adicionais)
    return usuario

@pytest.fixture
def banco_mock(mocker):
    banco = BancoDeDados()
    mocker.patch.object(banco,'buscar_usuario', return_value={"id": 1, "nome": "zill"})
    return banco

def test_sistema_principal(mocker, banco_mock):

    mock_response = mocker.patch('requests.get')
    mock_response.return_value.json.return_value = {"localização": "Estados_unidos"}
    

    resultado = sistema_principal(1, banco_mock)

    assert resultado == {"id": 1, "nome": "zill", "localização": "Estados_unidos"}
