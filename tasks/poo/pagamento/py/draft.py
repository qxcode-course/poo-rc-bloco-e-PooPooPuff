from abc import ABC
class Pagamento(ABC):
    def valor(self, valor:float,descricao:str):
        self.valor:float=valor
        self.descricao:str=descricao
    
    def resumo(self):
        print(f"Pagamento de R$ <{self.valor}>: <{self.descricao}>")
        
    def validar_valor(self):
        if self.valor<=0:
            raise ValueError("O Valor deve ser maior que zero")
        
    def processar(self):
        pass
    
class CartaoCredito(Pagamento):
    def __init__(self,valor:float,descricao:str,numero:int,nome_titular:str,limite_disponivel:float):
        super().__init__(valor,descricao)
        self.numero=numero
        self.nome_titular=nome_titular
        self.limite_disponivel=limite_disponivel
        
    def processar(self):
        if self.valor>self.limite_disponivel:
            raise Exception(f"Limite insuficiente no cartão {self.numero}")
        else:
            self.limite_disponivel-=self.valor
            print(f"Pagamento aprovado no cartão {self.nome_titular}")
            print(f"Limite restante: {self.limite_disponivel}")
            
class Boleto(Pagamento):
    def __init__(self,valor:float,descricao:str,codigo_barras:str,vencimento:str):
        super().__init__(valor,descricao)
        self.codigo_barras=codigo_barras
        self.vencimento=vencimento
    
    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")
        
class Pix(Pagamento):
    def __init__(self,valor:float,descricao:str,chave:str,banco:str):
        super().__init__(valor,descricao)
        self.chave=chave
        self.banco=banco
        
    def processar(self):
        print(f"PIX enviado via banco {self.banco} usando chave {self.chave}")
        
def processar_pagamento(pagamento:Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()
    
pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    CartaoCredito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    CartaoCredito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700),  # deve falhar
]

for pagamento in pagamentos:
    processar_pagamento(pagamento)