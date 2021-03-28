import sys

def driver_testcases():
    no_of_cases = int(input())
    for i in range(1, no_of_cases+1):
        arr = [x for x in input().split()]
        X,Y,mural = int(arr[0]) , int(arr[1]), arr[2]
        print(f"Case #{i}: {optimize_cost(X,Y,mural)}")

def optimize_cost(x, y, mural):
    """
    CJ: Cody Jamal pays X
    JC: Cody Jamal pays Y
    """
    cost_dict = {"CJ": x, "JC": y}

    total_cost = 0
    left =0 
    right =0
    size = len(mural)

    previous = 'X'
    for i in range(size):
        if previous == 'J' and mural[i] == 'C':
            total_cost += cost_dict["JC"]
        elif previous == 'C' and mural[i] == 'J':
            total_cost += cost_dict["CJ"]
        
        if mural[i] != '?':
            previous = mural[i]
    
    return total_cost

if __name__ == "__main__":
    driver_testcases()
