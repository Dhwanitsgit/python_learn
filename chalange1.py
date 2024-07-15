"""
odd = []
even_till5 = []
even_till20 = []
even_great20 = []

while True:
    user_input = input("Enter a number (or any text to exit): ")
    
    if user_input.isdigit():
        n = int(user_input)
        if n == 0:
            print("Oops, you entered 0. Exiting the loop.")
            break
    else:
        print("Non-integer input detected. Exiting the loop.")
        break 
    
    if n % 2 != 0: 
        print("Weird")
        odd.append(n)
    else:  
        if 2 <= n <= 5:
            print("Not Weird")
            even_till5.append(n)
        elif 6 <= n <= 20:
            print("Weird")
            even_till20.append(n)
        elif n > 20:
            print("Not Weird")
            even_great20.append(n)

print("List of odd numbers:", odd)
print("List of even numbers till range 5:", even_till5)
print("List of even numbers till range 20:", even_till20)
print("List of even numbers greater than 20:", even_great20)

# Nested loop to generate some values
generated_pairs = []
for i in odd:
    for j in range(i):
        generated_pairs.append((i, j + 1))

print("Generated pairs from odd numbers:", generated_pairs)

# Storing the generated pairs in a dictionary
d = {}
for key, value in generated_pairs:
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

print("Dictionary with generated pairs:", d)

"""
print("$",round((23456489.72948525479) * 2))