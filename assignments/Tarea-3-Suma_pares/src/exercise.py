import os
def main():
    os.system('clear')
    #SUMA DE NÚMEROS PARES HASTA EL 300
    Suma_pares=0
    for number in range(2,301,2):
        Suma_pares += number
    print(f"La suma de los números pares hasta el 300 es: {Suma_pares}")

if __name__=='__main__':
    main()
