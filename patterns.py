def print_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
rows=int(input("enter the no.of rows:"))
print_pattern(rows)