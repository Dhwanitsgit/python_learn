from decimal import Decimal
"""
principal = Decimal('100.00')
principal

rate = Decimal('0.05')
rate


for year in range(1,11):
    amount = principal*(1+rate) ** year
    print(f"{amount}")
    """
    
"""

num=2
sum = 0
for number in range(101):
    if number % 2 ==0:
        sum = sum + number 
    else:
        print(f"odd {number:.2f}")

print(sum , end='  ')
  """
"""

Tax= Decimal('6.25')
total_bill_amt = Decimal('37.54')
final_bill = total_bill_amt + ((Tax/ Decimal('100'))*total_bill_amt)

if Tax == Decimal('6.25'):
    print(f"The  {final_bill:>.2f}")
else:
    print(f"The  {final_bill:<.6f}")
"""

"""
DAta science 
thsn

grades = [23,4,45,65,76,5876,456,342,45,46,7,476,647467,4,765543,7,467,476,4424,647,4657,467,4333,4657,467,43,64,674,647,64,7,465,65,7,58,9,7899,8,9,89,6,8,76,8,765,54,765,8,765,88,765,8,65,78,657,8,6578,567,8,5]
print(f"THe sum is {sum(grades)}") 
print(f"{len(grades)}")
print(f"the avg or mean is {sum(grades)/ len(grades)}")

"""
# statics 
import statistics 
grades = [23,4,45,65,76,5876,456,342,45,46,7,476,647467,4,765543,7,467,476,4424,647,4657,467,4333,4657,467,43,64,674,647,64,7,465,65,7,58,9,7899,8,9,89,6,8,76,8,765,54,765,8,765,88,765,8,65,78,657,8,6578,567,8,5]
print(statistics.mean(grades))
print(statistics.median(grades))
print(statistics.mode(grades))
print(sorted(grades))
print(grades)