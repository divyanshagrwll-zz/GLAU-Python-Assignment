inp = int(input())

count =0
count=inp//5
inp = inp%5
if inp!=0:
    count = count+1
else:
    pass

print(count)