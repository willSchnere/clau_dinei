from atv_conta import *

def test_soma():
    assert soma (5,6) == 11
    assert soma (2,4) == 6
def test_subtrai():
    assert subtrai (2,1) == 1
    assert subtrai (40,20) == 20
def test_multiplica():
    assert multiplica(2,5) == 10
    assert multiplica(4,1) == 4
def test_divide():
    assert divide(2,0) == "Erro: divisão por zero não permitida."
    assert divide(10,2) == 5
def test_area_circulo():
    assert area_circulo (3) == math.pi*9
    assert area_circulo (-1) == "Erro: o raio não pode ser negativo."  
def test_area_retangulo():
    assert area_retangulo(5,4) == 20
    assert area_retangulo(-0,-10) == "Erro: largura e altura devem ser não-negativos."    
    
                  