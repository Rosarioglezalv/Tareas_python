import os
def main():
    os.system('clear')
    #CALCULA EL ÁREA Y PERIMETRO DE UN RECTÁNGULO
    print('AREA DE UN RECTANGULO')
    print('=====================')

    base=int(input('Dame la base:'))
    altura=int(input('Dame la altura:'))
    perimetro=2*(base+altura)
    perimetro='Perimetro='+str(perimetro)
    area=base * altura
    area='Area='+str(area)
    print(perimetro)
    print(area)


if __name__=='__main__':
    main()
