taxa_mortes = 0.06
taxa_nascimentos = 0.01
ano = 1599
população = int(input())
população_minima = população * 0.1

while população > população_minima:
    mortos = (população * taxa_mortes)
    nascidos = (população * taxa_nascimentos)
    ano += 1
    população += nascidos - mortos

    print(f'{ano},{nascidos:.0f},{mortos:.0f},{população:.0f}')

    
    
   
    


