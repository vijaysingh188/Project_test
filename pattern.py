print("a)")
def pypart(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
n = 5
pypart(n)

print("")
print("b)")
def print_pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i),"*"*(2*i-1))

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
