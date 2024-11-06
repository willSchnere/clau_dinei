import pytest

@pytest.fixture
def lista_simples():
    return [1,2,3,4,5]
def test_soma(lista_simples):
    assert sum(lista_simples) == 15
def test_tamanho(lista_simples):
    assert len(lista_simples) == 5
def test_indece(lista_simples):
    assert(lista_simples[4]) == 5   


