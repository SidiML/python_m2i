print("\t\t\t Table de multiplcation")
n=0
while n<=0:
    n = int(input("Saisir un nombre positif"))
for i in range(1, n+1):
    print(i,end="\t")
print(" ")
print("======="*11)
for j in range(1, n+1):
    for k in range(1, n+1):
        print(j * k,end="\t")
    print("\n")
