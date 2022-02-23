n = int(input('Enter The Number of Students : '))
x = [['Roll No','Name', 'Marks']]
for i in range(n):
    roll = input('Enter Roll No : ')
    name = input('Enter Student Name : ')
    marks = int(input('Enter Marks : '))
    x.append([roll, name, marks])
for i in range(len(x)):
    for j in range(len(x[i])):
        k=x[i][j]
        print(k, end='\t')
    print('\n')
y=int(input('Enter The Row to be Printed : '))
for i in x[y]:
    print(i, end='\t')
