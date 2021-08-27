import os
def main():
    os.system('clear')
    #CALCULA EL ÁREA DE UN TRAPECIO
    print('AREA DE UN TRAPECIO')
    print('===================')
    base1=float(input('Dame la base mayor:'))
    base2=float(input('Dame la base menor:'))
    altura=float(input('Dame la altura:'))
    area=((base1+base2)/2)*altura
    area='Area='+str(area)
    print(area)


if __name__=='__main__':
    main()
