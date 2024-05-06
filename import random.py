import random
 
def generuj_cisla_od_1_do_25():
 
    cisla = []
   
    for i in range(1, 26):
        cisla.append(i)
    return cisla

cisla_od_1_do_25 = generuj_cisla_od_1_do_25()

print("Vygeneroval si čísla od 1 do 25:", cisla_od_1_do_25)