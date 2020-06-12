fp = open("2.input.txt").readlines()
data = []
for line in fp:
    data.append(tuple(map(int,line.split(" "))))
k=data[0][0]
m=data[0][1]
sum=0
for i in range(1,k+1):
    sum+=int(data[i][data[i][0]])**2
print(sum%m)