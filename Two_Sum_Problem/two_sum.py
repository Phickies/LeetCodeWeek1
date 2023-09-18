import time

## INSERT THE FUNCTION HERE ##
def two_sum(n_list : list[int], target : int) -> list[int]:
    for i in range(len(n_list)):
        for j in range(i + 1, len(n_list)):
            if n_list[j] == target - n_list[i]:
                return [i, j]

## INSERT THE OPTIMIZED FUNCTION HERE ##
def two_sum_optimized(n_list: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(n_list)):
        hashmap[n_list[i]] = i
    for i in range(len(n_list)):
        complement = target - n_list[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]] 

list_count = input("How many number are there in your list: ")
num_list   = list()
for i in range(int(list_count)):
    num    = int(input("Your number at " + str(i) + " position is: "))
    num_list.append(num)

target_sum = int(input("your target sum: "))

start_time = time.time()

list_result = two_sum(n_list=num_list, target=target_sum)
# list_result = two_sum_optimized(n_list=num_list, target=target_sum)

## RUNTIME ##
print("--- %s seconds ---" % (time.time() - start_time))

print("Your list is: " + str(num_list))
print("Your two sum number position is: " + str(list_result))

## DEBUG COMMAND ##
