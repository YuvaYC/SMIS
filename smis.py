def marks():
	while True: 
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
	ml = menu.split()
	try: 
		if ml[0] == "add" and ml[1] == "sdt":
			name = input("Enter student's name: ")
			adrs = input("Enter student's address: ")
			city = input("Enter student's city: ")
			pc = int(input("Enter student's pincode: "))
			con = int(input("Enter student's Parent's/Guardian's Contact Number: "))
			yr = int(input("Enter student's year(1/2): "))
			comb = input("Enter student's combination: ")
			batch = input("Enter student's batch: ")
			rno = int(input("Enter student's Roll Number: "))
			print(f"""
			\t MAHESH PU COLLEGE
			Student Name: {name} \t Roll No.: {rno}
			Stream: {"Science" if comb == ("PCMC" or "PCMB") else "Commerce"} \t Combiination: {comb}
			Class: {yr} \t \t Batch: {batch}
			Address: {adrs}
			City: {city} \t \t Pin Code: {pc}
			Parent's/Guardian's Contact No.: {con}""")
			
		elif ml[0] == "add" and ml[1] == "marks":
			marks()
		elif menu.lower() == "attendance":
			attendance()
		elif menu == "help":
			print("""
		new\t\t\t add a new student
		marks\t\t\t operations related to marks of students
	
		marks:
		add\t\t\t add marks of a student
			
		help\t\t\t shows all commands
		""")
	except:
		continue
	else:
		break
'''def add(name, rno, 

print("""\t \t \t Student Management System
add                --- adding a new student
rmv <student_name> --- remove a specific student
see                --- list all the students
see <student_name> --- to see specific student details
""")

db = {}

while True:
	opn = input(">")
	opnl = opn.split()
	
	if opn == "add":
		
'''
