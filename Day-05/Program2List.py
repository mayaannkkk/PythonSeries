lis= []
num = int(input("Enter Number of students:"))
for i in range(num):
    lis.append(int(input(f"Enter {i+1} Student Marks:")))

lis.sort()

for i in lis:
    print(i,end=" ")