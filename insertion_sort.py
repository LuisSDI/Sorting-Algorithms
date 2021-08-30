from random import randint
import time

def insertSort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j - 1
        while (i >= 0 and array[i]< key):
            array[i+1] = array[i]
            i = i-1
        array[i+1]=key


n = int(input("Size of N: "))

array = []

for _ in range(n):
    array.append(randint(0,n))

tic = time.perf_counter()

print(array);
insertSort(array)
print(array);
toc = time.perf_counter()
print(f"The algorithm took {toc - tic:0.4f} seconds")


