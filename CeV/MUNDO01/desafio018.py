# Deve ser feita conversão de radioanos para seno usando a função match.readians()

import math
ang = int(input('Digite o valor do anglo: '))
senang = math.radians(ang)
sen = math.sin(senang)
cos = math.cos(senang)
tng = math.tan(senang)
print('O valor digitado foi {} \n seu seno é {:.2f} \n seu cos é {:.2f} \n e sua tangente é {:.2f}'.format(ang,sen,cos,tng))