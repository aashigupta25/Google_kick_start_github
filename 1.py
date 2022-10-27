# import math
# math.fmod(12.5, 5.5)

N = int(input("No. of bags"))
M = int(input("No. of kids"))

number_list = list(range(0, N))
no_of_toffees = sum(number_list)
print(no_of_toffees)

# print(math.fmod(no_of_toffees, M))

Remaining = no_of_toffees % M
print(Remaining)
