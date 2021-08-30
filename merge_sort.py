from random import randint
import time
n = int(input("Size of N: "))

def merge(array,p,q,r):
    n1 = q - p + 1
    n2 = r- q
    left = []
    right = [] 
    for i in range(0,n1):
        left.append(array[p+i])
    for j in range(0,n2):
        right.append(array[q+j + 1])
    left.append(n*2)
    right.append(n*2)
    i = 0 
    j = 0 
    k = p     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1
              

def mergeSort(array,p,r):
    if p < r:
        q = (p+r) // 2
        mergeSort(array,p,q)
        mergeSort(array,q+1,r)
        merge(array,p,q,r)
        
    


array = []

for _ in range(n):
    array.append(randint(0,n))

tic = time.perf_counter()

# print(array);
mergeSort(array,0,len(array)-1)
# print(array);
toc = time.perf_counter()
print(f"The algorithm took {toc - tic:0.4f} seconds")


