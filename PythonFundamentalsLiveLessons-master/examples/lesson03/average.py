
def user():
    list = [ ]
    grade = 0 
    while grade !=-1:
     grade = int(input("Enter the grades-1 for the exit: "))
     if grade != -1:
        list.append(grade)

    return list
def sum(list):
    sumr=0
    for i in list:
        sumr = sumr + i
    return sumr

def avg(list):
    avgr=0
    for i in list:
        avgr = (avgr/len(list)) + i
    return avgr
list =  user()
    
print(f"the sum is  {sum(list)}")
print(f'the avg is {avg(list):.2f}')