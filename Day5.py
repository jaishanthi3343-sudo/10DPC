

students = {"name": "Jai", "age": 35, "city": "chennai"}

students["age"]=36
print(students)

student = {"name": "Jai", "age": 35, "city": "chennai"}
student.pop("age")
print(student)

server = { "name": "webserver", "os": "Linux","port": 80}
print(server.keys())
print(server.values())

student = {"name": "Jai", "age": 35, "city": "chennai"}
for key,value in student.items():
    print(key,value)


student={"name":"jai","age":35}
name=input("enter your name")
age=int(input("enter your age"))

student={"name":"priya","age":30}
name=input("enter your name")
student["name"]=name
print(student)

age=int(input("enter your age"))
student["age"]=age
print(student)