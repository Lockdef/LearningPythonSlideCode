class math:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y

if __name__ == '__main__':
    
    math = math(1024, 2)
    
    print(math.addition())
    print(math.subtraction())
    print(math.multiplication())
    print(math.division())
