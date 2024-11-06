import requests

def obter_dados_da_api(url):
    resposta = requests.get(url)
    return resposta.json()

def test_obter_dados_da_api(mocker):
    
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.json.return_value = {"id":1,"nome":"Teste"}
    resultado = obter_dados_da_api("http://api.exemplo.com/dados")
    assert resultado == {"id":1,"nome": "Teste"}