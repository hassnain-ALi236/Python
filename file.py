# Write A file Through Python

f=open("demo.txt" , "w")
f.write("I am Ali Hassnain")
f.close()

# Read a File Throug Python

R=open("Sample.txt" , "r")
print(R.read())
R.close()


# Test Questions
p=open("Practice.txt", "w")
p.write("Hi EveryOne\nWe are Learning Python\nusing Java\nI like to wirte Program in java.")
p.close()

# Replace Java Text With Python
g=open("Practice.txt", "r")
data=g.read()
newData=data.replace("Java", "Python")
print(newData)
def chcek_for_line():
    word="e"
    data=True
    lineno=1
    f=open("Practice.txt", "r")
    while data:
        data=f.readline()
        if(word in data):
            print(lineno)
            return
            lineno+=1
    return -1
print(chcek_for_line())