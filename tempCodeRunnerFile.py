even_count = 0
odd_count = 0
for i in range(1, 11):
    num = int(input(f"Number {i} enter karein: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Total Even Numbers: {even_count}")
print(f"Total Odd Numbers:  {odd_count}")