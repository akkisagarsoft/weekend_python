# employee_file = open("C:\Users\Gaurav Akshay\PycharmProjects\weekend1_python\filehandling\employee.txt",mode='r',encoding='utf-8')
import json
emp = open("employee.txt", "r+w",encoding="utf-8")
try:
 emp.write("adding things from program")
 for emmployee in emp.readlines():
    print(emmployee)
finally:
    emp.close()




# json_file = open("movie.json","r",encoding="utf-8")
# movie = json.load(json_file)