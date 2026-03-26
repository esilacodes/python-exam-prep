
"""
Question: Find all 3-digit Armstrong numbers
Logic: Take the digits → cube each digit → sum them → check if equal to the number
Difficulty: Medium
"""


#IN MY PERSPECTIVE******************************

start=100
finish=1000
list=[]
for i in range(start,finish):
    str_num=str(i)
    summm=0


    for j in str_num:
        num=int(j)
        summm+=num**3

    if(summm==i):
        list.append(i)

print(list)
print(len(list))


#************************************************

# WITH INPUT()

startnum=int(input("start:"))
finishnum=int(input("finish:"))
armstronglist=[]
for i in range(startnum,finishnum):
    summ=sum(int(d)**3 for d in str(i))  #get number and calculate cube and sum  ------>generator expression 
    if summ==i:
        armstronglist.append(i)
print(armstronglist)
print(len(armstronglist))

