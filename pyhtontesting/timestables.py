n = int(input("What size of table do you want to generate? "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(str(i*j)+"\t", end="")
    print()