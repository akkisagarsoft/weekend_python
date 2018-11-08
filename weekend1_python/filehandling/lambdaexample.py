g = lambda x: 3*x+1
full_name = lambda fn, gn: fn.strip().title() + " " + gn.strip()

def mytest(f,num):

 output = g(num)
 print(output)
 print(full_name("Akshay", "Rastogi"))

if __name__ == '__main__':
     mytest(g,34)