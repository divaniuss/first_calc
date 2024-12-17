class Calculator:
    def init(self,a,b):
        self._a=a
        self._b=b

    def Addition(self):
        return f"{self._a} + {self._b} = {self._a+self._b}"

    def Subtraction(self):
        return f"{self._a} - {self._b} = {self._a - self._b}"

    def Multiplication(self):
        return f"{self._a} * {self._b} = {self._a * self._b}"

    def Division(self):
        if self._b != 0:
            return f"{self._a} / {self._b} = {self._a / self._b}"
        return "Division on zero is impossible"

c = Calculator(3,5)
print(c.Addition())