from operaciones import sumar,restar
import pytest
def saludar(nombre):
    print("hola "+nombre)

def main():
    saludar("Allison")
    print(sumar(7))
    print(sumar(7,5))
    saludar("Maria")
    print(restar(5,7))

def test_resta():
    assert restar(10,5)==5
    assert restar(5,5)==0
    assert restar(0,5)==-5

def test_suma():
    assert sumar(7)==10

if __name__=="__main__":
    main()