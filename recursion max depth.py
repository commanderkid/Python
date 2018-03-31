#Integer Factorization

"""Fundamental Theorem of Arithmetic states that any integer could
be represented as product of one or more primes and such
representation is unique"""



def Ranger(number, massodd, chislo = 2, otvet = []):
    if (number % chislo == 0) and (number > chislo): 
        number /= chislo
        otvet += [chislo, '*']
        #print("1 " + str(otvet) + " " + str(chislo))
        return Ranger(number, massodd, chislo, otvet)
    elif number == chislo:
        otvet.append(chislo)
        #print("2 " + str(otvet) + " " + str(chislo))
        return otvet
    elif number % chislo != 0:
        chislo += 1
        #print("3 " + str(otvet) + " " + str(chislo))
        return Ranger(number, massodd, chislo, otvet)
        


obshii = []
for i in range(int(input())):
    number = int(input())
    massodd = [int(i) for i in range(2, number)]
    print(Ranger(number, massodd))
