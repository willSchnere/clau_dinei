import pytest

def soma_dobro(numeros):    
    return sum( x * 2 for x in numeros)

@pytest.fixture
def lista_numeros():
    return [10,20,40]

def test_soma_dobro(lista_numeros):
    #resultado = soma_dobro(lista_numeros)
    #assert resultado (lista_numeros) == 30 
    assert soma_dobro(lista_numeros) == 140

