n = int(input("Enter the number of students: "))

smis = {}

def student(name, rollno, percentage):
	std = smis.update({name: [rollno, percentage]})
	return std

count = 0

while count < n:
	name = input("Enter student name: ")
	rollno = int(input("Enter student Roll Number: "))
	percent = float(input("Enter student pecentage: "))
	
	hi = student(name, rollno, percent)
	
	count+=1
	
print(smis)

