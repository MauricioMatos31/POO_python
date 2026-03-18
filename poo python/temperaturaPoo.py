import sys
import os

class controleTemperatura:
    def __init__ (self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
     return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if valor < -50 or valor > 100:
            raise ValueError("Temperatura fora do intervalo permitido (-50 a 100 graus Celsius)")
        self.__temperatura = valor

    def converter_para_fahrenheint(self):
       return self.__temperatura * 9/5 + 32   


temperatura = controleTemperatura(float(input("Digite a temperatura em Celsius: ")))

print(f"Temperatura em Celsius: {temperatura.temperatura}°C")


print(f"Temperatura em Fahrenheit: {temperatura.converter_para_fahrenheint()}°F")