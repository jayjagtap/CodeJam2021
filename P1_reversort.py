import sys

def driver_testcases():
    no_of_cases = int(input())
    for i in range(1, no_of_cases+1):
        length = int(input())
        arr = [int(x) for x in input().split()]
        print(f"Case #{i}: {Reversort(arr)}")

def main():
    Reversort(L)

def Reversort(L):
    
    cost = 0
    l = len(L)
    for i in range(0, l-1):
        j = get_smallest(L,i)
        reverse_array(L,i,j)
        cost += j-i +1
    
    return cost

def get_smallest(array, start):
    smallest = array[start]
    index  = start
    for i in range(start+1, len(array)):
        if array[i] <= smallest:
            smallest = array[i]
            index = i
    
    return index

## Correct
def reverse_array(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start+=1
        end-=1
    
    return array

if __name__ == "__main__":
    driver_testcases()
    # print(reverse_array([5,6,7,8,3,5, 9], 2,5))
    # print(get_smallest([5,6,7,8,3,5, 9],2))

