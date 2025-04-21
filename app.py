from operaciones import sumar

def saludar(nombre):
    print("hola "+nombre)

def main():
    saludar("Allison")
    print(sumar(7))
    print(sumar(7,5))

if __name__=="__main__":
    main()