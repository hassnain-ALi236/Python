name=input("Enter Your Name : ")
birth_Year=int(input("Enter Your Birth Year : "))
current_Year= int(input("Enter Current Year : "))
age=-birth_Year+current_Year
print(f"Hello {name} Your are {age} Old")
 
# Task 02

n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
n3=int(input("Enter Third Number : "))
print(f"Your Largest Number is --> {max(n1,n2,n3,)}")

# Task -3

total=0
for i in range (1,50):
    if(i%3==0 or i % 5==0):
        digits=i%10
        total+=digits
        i=i//10
print(total)

# Task 04
def check_palindrome():
    st="madam"
    st.capitalize()
    rev_st = st[::-1]
    if(st==rev_st):
        print(st,"String is Palindrome")
    else:
        print( st,"String is Not Palindrome")

check_palindrome()

def get_event(number_list):
    for i in number_list:
        print(f"My Number is list is here --> {number_list}")
get_event(1,4,6,2)


# Task 07
group_a = ["Ali", "Zara", "Ahmed", "Bilal", "Ali"]
group_b = ["Ahmed", "Sara", "Bilal", "Usman"]
set(group_a)== group_a
set(group_b)== group_b
print(set(group_a).intersection(set(group_b)))
set1=(set(group_a).union(set(group_b)))
((set1))==set1
print(set1)
print((type(set1)))