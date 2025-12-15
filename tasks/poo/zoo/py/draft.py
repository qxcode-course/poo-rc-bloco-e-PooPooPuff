from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name:str="")->None:
        self.name:str=name
    
    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.name}")
        
    def fazer_som(self)->None:
        pass
    
    def mover(self)->None:
        pass
        
class Liao(Animal):
    def __init__(self,name:str)->None:
        super().__init__(name)
        
    def fazer_som(self):
        print("RAAAHWRRRR")
        
    def mover(self):
        print("*correndo no mei dos mato*")
    
class Pexe(Animal):
    def __init__(self,name:str)->None:
        super().__init__(name)
        
    def fazer_som(self):
        print("BLUB BLUB")
    
    def mover(self):
        print("*nadando pra comer a minhoca*")

class Mukito(Animal):
    def __init__(self,name:str)->None:
        super().__init__(name)
    
    def fazer_som(self):
        print("BBBBZZZZZZZZZZZZZZZZZZZ")
        
    def mover(self):
        print("*fazendo bzz enquanto voa, ate morrer pra raquete eletrica*")

def apresentar(animal:Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"eu sou do tipo :{type(animal).__name__}")
    print("|||"+("\/"*20)+("|||"))


Animais:list[Animal]=[Liao("fortaleza"),Pexe("Peixonauta"),Mukito("e a muriçoka pica pica pica")]
for animal in Animais:
    apresentar(animal)