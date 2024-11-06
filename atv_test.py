from atv_primeira import *

def test_email_verifica():
    assert email_valido ("testemail@gmail.com") == True
    assert email_valido ("false@gmail") == False

def test_numero_par():
    assert eh_par (4) == True
    assert eh_par (1) == False
def test_fatorial():
    assert fatorial (5) == 120
    assert fatorial (0) == 1

def test_quadrado():
    assert quadrado (2) == 4
    assert quadrado (5) == 25
def test_eh_positivo ():
    assert eh_positivo (1) == True
    assert eh_positivo (-10) == False
def test_verifica_maioridade():
    assert verificar_maioridade (20) == "maior de idade"
    assert verificar_maioridade (15) == "menor de idade"
def test_classificar_temp():
    assert classificar_temperatura(-25) == "frio"
    assert classificar_temperatura(20) == "moderado"
    assert classificar_temperatura (32) == "quente"
def test_avaliar_nota():
    assert avaliar_nota (8) == "aprovado"
    assert avaliar_nota (6) == "recuperacao"
    assert avaliar_nota (4) == "reprovado"
def test_voto():
    assert pode_votar (22) == "voto obrigatório"
    assert pode_votar (17) == "voto facultativo"
    assert pode_votar (15) == "não pode votar"
def test_avaliar_produto():
    assert avaliar_produto (5) == "excelente"
    assert avaliar_produto (4) == "bom"
    assert avaliar_produto (3) == "regular"        
    assert avaliar_produto (2) == "ruim"        
    assert avaliar_produto (1) == "péssimo"
    assert avaliar_produto (0) == "valor inválido"                                         