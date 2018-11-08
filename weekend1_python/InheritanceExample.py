# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):
    def __init__(self):
        # calling super function
        super().__init__()
        print("Penguin is ready")

    def whoIsThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


if __name__ == '__main__':
    peggy = Penguin()
    peggy.whoIsThis()
    peggy.swim()
    peggy.run()