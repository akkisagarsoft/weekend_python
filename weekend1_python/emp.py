emp = open("C:\Users\Gaurav Akshay\PycharmProjects\weekend1_python\employee.txt","r")
for employee in emp.readlines():
    print(employee)

emp.close()