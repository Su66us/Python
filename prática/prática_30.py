print('Analisador de Triângulos')
r1 = float(input('O primeiro segmento: '))
r2 = float(input('O segundo segmento: '))
r3 = float(input('O terceiro segmento:'))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um Triãgulo')
else:
    print('Os segmentos acima não  podem formar um Triâgulo')