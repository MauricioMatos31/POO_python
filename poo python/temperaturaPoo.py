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
        self.__temperatura = valor

    def converter_para_fahrenheint(self):
       return self.__temperatura * 9/5 + 32   

try:
    temperatura = controleTemperatura(float(input("Digite a temperatura em Celsius: ")))
    if temperatura.temperatura < -50 or temperatura.temperatura > 100:
        raise ValueError("Temperatura fora do intervalo permitido (-50 a 100 graus Celsius)")
    print(f"Temperatura em Celsius: {temperatura.temperatura}°C")
    print(f"Temperatura em Fahrenheit: {temperatura.converter_para_fahrenheint()}°F")
except ValueError as e:
    print(f"Erro: {e}")     
     