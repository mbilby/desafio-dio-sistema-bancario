class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_dia()) >= 10:
            print("\n@@@ Limite de transações atingido! @@@")
            return
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)