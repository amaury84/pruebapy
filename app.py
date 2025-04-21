from operaciones import sumar,restar

def saludar(nombre):
    print("hola "+nombre)

def main():
    saludar("Allison")
    print(sumar(7))
    print(sumar(7,5))
    saludar("Maria")
    print(restar(5,7))

if __name__=="__main__":
    main()