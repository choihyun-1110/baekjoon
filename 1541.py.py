
# N=input().split('-')
# list=[]
# sum=0
# for i in N:
#     N[i].split('+')
#     for j in N[i]:
#         sum=sum+int(N[i][j])
#         list.append(sum)
# sum_1 = list[0]
# for i in range(1,len(sum)):
#     sum_1 = sum_1-list[i]
# print(sum_1)




# N=input().split('-')
# list=[]
# sum=0
# for i in N:
#     tmp=N[i].split('+')
#     for j in tmp:
#         sum+=int(j)
#         list.append(sum)
# sum_1 = list[0]
# for i in range(1,len(sum)):
#     sum_1 -=list[i]
# print(sum_1)

# N=input().split('-')
# list=[]

# for i in N:
#     sum=0
#     tmp=N[i].split('+')
#     for j in tmp:
        
#         sum+=int(j)
#         list.append(sum)
# sum_1 = list[0]
# for i in range(1,len(sum)):
#     sum_1 -=list[i]
# print(sum_1)


N=input().split('-')
list=[]

for i in N:
    sum=0
    tmp=i.split('+')
    for j in tmp:
        sum +=int(j)
    list.append(sum)

s= list[0]
for i in range(1,len(list)):
    s -=list[i]
print(s)

