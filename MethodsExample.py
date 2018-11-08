class Parrot:
    # instance attributes
    def __init__(self,name,age):
        self.name = name
        self.gae = age

    # instance method
    def sing(self,song):
        return "{}  sings {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)

if __name__ == '__main__':
    blu = Parrot("Blu",10)

    # call instance methods
    print(blu.sing("'Happy'"))
    print(blu.dance())

