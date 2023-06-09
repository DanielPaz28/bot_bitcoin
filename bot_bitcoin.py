import ssl
import json

import websocket
import bitstamp.client

import credenciais_exemplos


def cliente():
    return bitstamp.client.Trading(username=credenciais_exemplos.USERNAME, key=credenciais_exemplos.KEY, secret=credenciais_exemplos.SECRET)


def comprar(quantidade):
    trading_client = cliente()
    trading_client.buy_market_order(quantidade)


def vender(quantidade):
    trading_client = cliente()
    trading_client.buy_market_order(quantidade)


def ao_abrir(ws):
    print("Abriu a conexão")

    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd", "auth": "[token]"
    }
}
"""
    ws.send(json_subscribe)


def ao_fechar(ws):
    print("Fechou a conexão")


def erro(ws, erro):
    print("Deu erro")
    print(erro)


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = (mensagem["data"]["price"])
    print(price)

    if price > ("Digite o valor"):
        vender()

    elif price < ("Digite o valor"):
        comprar
    else:
        print("Aguardar")


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_error=erro,
                                on_message=ao_receber_mensagem)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}) 
