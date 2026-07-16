def new():
	name = input("Enter student's name: ")
	roll_no = int(input("Enter student's Roll Number: "))
	cls = int(input("Enter student's class(11/12): "))
	batch = input("Enter student's batch: ")
	adrs = input("Enter student's address: ")
	city = input("Enter student's city: ")
	pincode = int(input("Enter student's pincode: "))
	contact = int(input("Enter student's Parent's/Guardian's Contact Number: "))

	print(f"""
	\t MAHESH PU COLLEGE
	Student Name: {name} \t Roll No.: {roll_no}
	Class: {cls} \t \t Batch: {batch}
	Address: {adrs}
	City: {city} \t \t Pin Code: {pincode}
	Parent's/Guardian's Contact No.: {contact}
	""")

def marks():
	marks = input("marks>")
	while True: 
		if marks == "add":
			name = input("Enter student's name: ")
			phy = int(input("Physics: "))
			chem = int(input("Chemistry: "))
			maths = int(input("Mathematics: "))
			eng = int(input("English: "))
			total = phy+chem+maths+eng
			pcent = (total/300)*100
			grade = "A" if pcent >= 85 else "B" if pcent >= 75 and pcent < 85 else "C" if pcent >= 50 and pcent < 75 else "D" if pcent >= 30 and pcent < 50 else "F"
		
			print(f"""
			Student: {name}
			Phsyics: {phy}/70
			Chemistry: {chem}/70
			Mathematics: {maths}/80
			English: {eng}/70
			Total = {total}/300 --- {pcent}%
			Grade = {grade}
			""")
		elif menu == "help":
			print("""
			new\t\t\t add a new student
			marks\t\t\t operations related to marks of students
		
			marks:
			add\t\t\t add marks of a student
				
			help\t\t\t shows all commands
			""")
		else: break

def attendance():
	while True:
		pre = input("Enter the number of days present: ")
		
		if pre.lower() == "exit":
			break
		elif pre == '':
			continue
		working_days = int(pre)/24
		if working_days >= 0.78:
			print("The student is a defaulter")
		else:
			print("The student is short of attendance")
			

print("		Mahesh PU College - Student Management System")
print('''
type \"help\" for more information\"
''')
while True:
	menu = input(">")
	if menu.lower() == "new":
		new()
	elif menu.lower() == "marks":
		marks()
	elif menu.lower() == "attendance":
		attendance()
	else:
		break

