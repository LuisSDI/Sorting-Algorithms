from random import randint
import time

def selectionSort(array):
    for j in range(len(array)-1):
        index = j
        small = array[j]
        for i in range(j+1,len(array)):
            if array[i] < array[index]:
                index=i
        array[j]= array[index]
        array[index]=small
                


n = int(input("Size of N: "))

array = []

for _ in range(n):
    array.append(randint(0,n))

tic = time.perf_counter()

print(array);
selectionSort(array)
print(array);
toc = time.perf_counter()
print(f"The algorithm took {toc - tic:0.4f} seconds")