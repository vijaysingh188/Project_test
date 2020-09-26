def print_number(n):
    for i in range(1,n+1):    #i represents no. of rows
        for j in range(1,i+1):  #j represnts no. of *
            print("*",end=" ")
        print()
# print_number(5)
def print_pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i),"*"*(2*i-1))
#
# print_pattern(5)
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
# rows = 6
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")
#
# # print(" ")
#
# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")