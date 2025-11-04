"""
a = 2
b = 3
sum = a + b
print("Sum is:", sum)
"""
n = int(input("Enter no. "))
i = 1
while i <=10:
    print(n, " * ",i, " = ", i*n)
    i += 1

def fact(n):
    if(n == 1 or n==0):
        return 1
    return fact(n-1) * n
print("Factorial of ", n , " = ", fact(n))

fruitList = ["Mango","Orange","Guava","Grapes","Banana"]
def Print_list(lst, indx=0):
    if(indx == len(lst)):
        return
    if(indx == len(lst)-1):
        print(lst[indx])
    else:
        print(lst[indx], end=", ")
    Print_list(lst, indx+1)

Print_list(fruitList)

def ceck_for_line():
    word ="JAVA"
    data = True
    line_no = 1
    count = 0
    with open("Practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                count += 1
                print("The Word '", word, "' exist at line: ", line_no, sep="")
            line_no += 1
    if(count == 0):
        print("The Word '", word, "' not found", sep="")
        
ceck_for_line()