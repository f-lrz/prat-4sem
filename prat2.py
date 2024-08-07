import math

A_carla = 1.85
A_fernanda = 1.65
M_carla = 80
M_fernanda = 112

if A_carla > A_fernanda:
    print("Carla é maior que Fernanda")
elif A_carla < A_fernanda:
    print("Carla é menor que Fernanda")
else:
    print("Carla tem a mesma altura que Fernanda")

IMC_carla = M_carla / (math.pow(A_carla, 2))
IMC_fernanda = M_fernanda / (math.pow(A_fernanda, 2))

I = IMC_carla

print("Carla ",  end="")

if I < 17:
    print("está muito abaixo do peso.")
elif I >= 17 and I <= 18.49:
    print("está abaixo do peso.")
elif I >= 18.5 and I <= 24.99:
    print("está com o peso normal.")
elif I >= 25 and I <=29.99:
    print("está acima do peso.")
elif I >= 30 and I <= 34.99:
    print("está com obesidade I.")
elif I >= 35 and I <= 39.99:
    print("está com obesidade II (severa).")
else:
    print("está com obesidade III (mórbida).")


I = IMC_fernanda

print("Fernanda ",  end="")

if I < 17:
    print("está muito abaixo do peso.")
elif I >= 17 and I <= 18.49:
    print("está abaixo do peso.")
elif I >= 18.5 and I <= 24.99:
    print("está com o peso normal.")
elif I >= 25 and I <=29.99:
    print("está acima do peso.")
elif I >= 30 and I <= 34.99:
    print("está com obesidade I.")
elif I >= 35 and I <= 39.99:
    print("está com obesidade II (severa).")
else:
    print("está com obesidade III (mórbida).")

lista1 = [1,4, 7, 10, 13, 16]
lista2 = [2, 4, 8, 16, 32, 64]

soma = 0
i = 0

for i in lista1:
    soma = soma + i
print("\n", soma)

soma = 0
i = 0

while i < len(lista2):
    soma = soma + lista2[i]
    i = i + 1
print(soma)