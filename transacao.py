from utils import verificar_numero_saques

def deposito(valor, saldo):
    
    saldo =+ valor
    return saldo

def registrar_extrato(valor, extrato):

    extrato += f"Depósito: R$ {valor:.2f}\n"
    return extrato

def saque(valor, saldo):

    saldo -= valor
    return saldo