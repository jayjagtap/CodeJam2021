import itertools
import sys

def driver_testcases():
    no_of_cases = int(input())
    for i in range(1, no_of_cases+1):
        arr = [int(x) for x in input().split()]
        N,C = arr[0], arr[1]
        answer = check_score(N,C)
        if answer == "IMPOSSIBLE":
            print(f"Case #{i}: {answer}")
        else:
            print(f"Case #{i}: {' '.join(str(x) for x in answer)}")

def check_score(N,C):

    base_list = [i for i in range(1, N+1)]
    answer = "IMPOSSIBLE"
   
    for i in itertools.permutations(base_list, len(base_list)):
        score = Reversort(list(i))
        if score == C:
            return list(i)

    return answer


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





