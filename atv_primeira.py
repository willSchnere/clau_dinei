import math

def email_valido(email):
    return '@' in email and '.' in email

def eh_par(n):
    return n % 2 == 0

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

def quadrado(n):
    return n ** 2

def eh_positivo(n):
    return n > 0

def verificar_maioridade(idade):
    if idade >= 18:
        return 'maior de idade'
    else:
        return 'menor de idade'

def classificar_temperatura(temp):
    if temp < 0:
        return 'frio'
    elif 0 <= temp <= 25:
        return 'moderado'
    else:
        return 'quente'

def avaliar_nota(nota):
    if nota >= 7:
        return 'aprovado'
    elif 5 <= nota < 7:
        return 'recuperacao'
    else:
        return 'reprovado'

def pode_votar(idade):
    if idade >= 18:
        return 'voto obrigatório'
    elif 16 <= idade < 18:
        return 'voto facultativo'
    else:
        return 'não pode votar'

def avaliar_produto(estrelas):
    if estrelas == 5:
        return 'excelente'
    elif estrelas == 4:
        return 'bom'
    elif estrelas == 3:
        return 'regular'
    elif estrelas == 2:
        return 'ruim'
    elif estrelas == 1:
        return 'péssimo'
    else:
        return 'valor inválido'

