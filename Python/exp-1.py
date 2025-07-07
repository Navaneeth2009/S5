#Hello World
print("Hello,World!")
print("Welcome to python programming")
#Basic Data Types and Operations
a=10
b=5.5
c="Python"
print(f"a:{type(a)},b:{type(b)},c:{type(c)}")
print(f"a+b :{a+b}")
print(c+" is fun!")
#Arithmetic Operations
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")
print(f"{a}**{b}={a**b}")
#Boolean Logic
is_sunny=True
have_umbrella=False
def checkp(sun,umb):
	print("Should you go outside? : ",sun|umb)
	if(sun!=True):
		print("Should you carry umbrella? : Yes ")
	else:
		print("Should you carry umbrella? : No ")
checkp(is_sunny,have_umbrella)
#String Operations
in1=input("Enter a sentence : ")
print("No. of characters : ",len(in1))
print("Lowercase string : ",in1.lower())
print("Uppercase string : ",in1.upper())
print(in1.replace(" ","_"))
ck=0
parts=in1.split()
for ch in parts:
	if ch=="Python":
		ck=1
if ck==True:
	print("Word 'Python' present")
else:
	print("Word 'Python' not present")
#Control Structures if
num=int(input("Enter a number : "))
if num>0:
	print("Positive number")
elif num<0:
	print("Negative number")
else:
	print("Zero")
#Control Structures if-elif-else
print("GRADE OF STUDENT")
m=int(input("Enter student mark : "))
if 90<=m<=100:
	print("Grade A")
elif 75<=m<=89:
	print("Grade B")
elif 60<=m<=74:
	print("Grade C")
elif 40<=m<=59:
	print("Grade D")
else:
	print("Fail")
#Mini Calculator
print("MINI CALCULATOR")
n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
c="1"
while(c!="0"):
	op=input("Enter operation [+,-,*,/] : ")
	if op=="+":
		print(f"{n1}+{n2}={n1+n2}")
	elif op=="-":
		print(f"{n1}-{n2}={n1-n2}")
	elif op=="*":
		print(f"{n1}*{n2}={n1*n2}")
	elif op=="/":
		if n2==0:
			print("Division by zero not possible")
		else:
			print(f"{n1}/{n2}={n1/n2}")
	else:
		print("Invalid option")
	c=input("Enter '0' to stop calculation.")
