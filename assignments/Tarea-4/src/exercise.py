import os
from math import factorial
def main():
    os.system('clear')
    #FACTORIAL DE UN NÚMERO NO NEGATIVO
    for i in range(1,4): 
        valor = int(input("Dame un número no negativo="))
        while (valor >= 0):
             num_factor=factorial(valor)
             print(str(valor)+"!="+str(num_factor))
             break
        if (valor < 0):
            print(str(valor)+"!=ERROR!")
        i=i+1

if __name__=='__main__':
    main()
