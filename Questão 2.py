taxa = 1.004
rende = 1.007
preço = float(input())
poup = 10000
mes = 0

while preço > poup:
    poup *= rende
    preço *= taxa
    mes+=1

print(mes)
