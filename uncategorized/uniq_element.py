    """https://practice.geeksforgeeks.org/problems/find-unique-element/0
    """
cases = int(input())

for c in range(cases):
    n,k = list(map(int, input().split()))
    integers = input().split()

    counter = {}

    for i in integers:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] = counter[i] + 1

    for key,value in counter.items():
        if value == 1:
            print(key)
