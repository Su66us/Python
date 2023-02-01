
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "tutular": titular,
             "slado": saldo, "limite": limite}
    return conta


def deposita(conta, valor): 
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("O saldo é {}".format(conta['saldo']))
