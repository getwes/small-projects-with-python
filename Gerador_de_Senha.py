import random

cmax = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
cmin = "abcdefghijklmnoprstuvwxyz"
num = "0123456789"
cEsp = "!@#$%&"

composicao = cmax + cmin + num + cEsp

digitos = 15

senha1 = "".join(random.sample(composicao,digitos));
senha2 = "".join(random.sample(composicao,digitos));
senha3 = "".join(random.sample(composicao,digitos));

print('senha: ' + senha1)
print('senha: ' + senha2)
print('senha: ' + senha3)