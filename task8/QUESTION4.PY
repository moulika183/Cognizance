import pandas as pd
result=''
x=int(input("Enter The Length Of The Array:"))
y=[input("Enter The Element:") for i in range(x)]
z=pd.Series(y)
for i in range(len(y)):
    result+=(" "+z[i])
print(result.title())
if x==y:
    print("True")
