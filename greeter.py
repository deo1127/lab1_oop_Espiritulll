class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}! Welcome to OOP in Python."


if __name__ == "__main__":
    hello = Greeter("Student")
    print(hello.greet())