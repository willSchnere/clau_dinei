import requests

class BancoDeDados:
    def buscar_pedido(self, pedido_id):
        raise NotImplementedError("Consulta real ao banco de dados")

def calcular_valor_total(pedido_id):
    resposta = requests.get(f"http://api.loja.com/pedidos/{pedido_id}")
    dados_produtos = resposta.json()
    total = sum(item["preco"] * item["quantidade"] for item in dados_produtos)
    return total

def obter_pedido_com_valor_total(pedido_id, banco):
    pedido = banco.buscar_pedido(pedido_id)
    valor_total = calcular_valor_total(pedido_id)
    pedido["valor_total"] = valor_total
    return pedido