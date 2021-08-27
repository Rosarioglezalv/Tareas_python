import os
def main():
    #PROMEDIO DE LOS NÚMEROS DE LA LISTA
    os.system('clear')
    Promedio = 0   
    Lista = [4,3,7,2,9,10,15,1,6,7,2,1,20,5,8]
    for i in Lista:
        Promedio = Promedio + i
    
    Promedio= Promedio/len(Lista)
    print(f"El pomedio de los número de la lista es: {Promedio}")
if __name__=='__main__':
    main()
