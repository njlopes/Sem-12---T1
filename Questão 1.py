vel_l = 10
vel_t = 1
lebre = 0
tartaruga = int(input())
minuto = 0

while tartaruga > lebre:
    tartaruga += vel_t
    lebre += vel_l
    minuto += 1

print(minuto)
