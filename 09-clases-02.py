import os
class operasBas:
    n1=0
    n2=0
    res=0
    def sumar(self):
        self.res=self.n1+self.n2
        return self.res
    
    def resta(self):
        self.res=self.n1-self.n2
        return self.res
    
    def multi(self):
        self.res=self.n1*self.n2
        return self.res
    
    def dividir(self):
        self.res=self.n1/self.n2
        return self.res
    
    def pedirNum(self):
        self.n1= int(input("n1: "))
        self.n2= int(input("n2: "))

    def imprimir(self):
        print("El resultado es: ",self.res)
     
     
     
obj= operasBas()
       
def menu():
    op=0
    while op !=5:
        os.system("cls")
        print("1.- +\n2.- -\n3.- *\n4.- \n5.- SaLIR\n")
        op= int(input("Opcion: "))
        if op == 1:
            obj.pedirNum()
            obj.sumar()
            obj.imprimir()
            input()
        if op==2:
            obj.pedirNum()
            obj.resta()
            obj.imprimir()
        if op==3:
            obj.pedirNum()
            obj.multi()
            obj.imprimir()


if __name__=="__main__":
    menu()

