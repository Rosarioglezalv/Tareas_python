import os
def main():
    os.system('clear')
    #CALCULA EL ÁREA DE UN TRIÁNGULO
    print('ÁREA DE UN TRIÁNGULO')
    print('========================')
    base=float(input("Dame la base: "))
    altura=float(input("Dame la altura: "))
    area=(base*altura)/2
    print('Área del Triángulo=',area)


if __name__=='__main__':
    main()
