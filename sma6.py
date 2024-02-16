#6
from random import *
number=[]
N=int(input("mitu numbrit on nimekirjas? "))
for o in range(N):
    number.append(randint(1,1000))
print(number)
max_num=max(number)
print("max numbri:", max_num)
kasutu=max_num / N
print("kasutu number:", kasutu)
index_max_num = number.index(max_num)
number[index_max_num] = kasutu
print("Numbrite loend pärast muutmist:", number)

#7
from random import *
try:
    arv=[]
    N=int(input("mitu numbrit on nimekirjas? "))
    for i in range(N):
        arv.append(randint(1,100))
    arv.sort()
    print(arv)
    arv.sort(reverse=True)
    print(arv)
except ValueError:
    print("Error")

#12
from random import *
try:
    numbers=[]
    for y in range(10):
        numbers.append(randint(1,100))
    print(numbers)
    max_arv=max(numbers)
    min_arv=min(numbers)
    print("maksimaalne ja minimaalne arv:", max_arv, min_arv)
    index_max=numbers.index(max_arv)
    numbers[index_max]=min_arv
    index_min=numbers.index(min_arv)
    numbers[index_min]=max_arv
    print("muudetud nimekiri", numbers)
except ValueError:
    print("Error")

#11


