import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}'. format(ang, seno))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}'. format(ang, cos))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o Tangente de {:.2f}'. format(ang, tan))
# Resolução do Guanabara 
# from math import radians, tan, sin, cos
# ang = float(input('Digite o ângulo que você deseja: '))
# seno = sin(radians(ang))
# print('O ângulo de {} tem o Seno de {:.2f}'. format(ang, seno))
# cos = cos(radians(ang))
# print('O ângulo de {} tem o Cosseno de {:.2f}'. format(ang, cos))
# tan = tan(radians(ang))
# print('O ângulo de {} tem o Tangente de {:.2f}'. format(ang, tan))
