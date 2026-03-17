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
