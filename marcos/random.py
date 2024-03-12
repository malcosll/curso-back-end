import random 
import time

intervalo_tempo = 5
time.sleep(intervalo_tempo)
a = 1
b = 10

numero_aleatorio = random.randint (a,b)
print("O número aleatório no intervalo [",a, ",", b,"]:" , numero_aleatorio)