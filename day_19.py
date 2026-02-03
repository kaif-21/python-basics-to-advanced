'''Common Operator Overloading Magic Methods

__add__(self.other):adds two object using the + operators
__sub__(self.other):subtract two object using the - operators
__mul__(self.other):multiply two object using the * operators
__truediv__(self.other):divide two object using the / operators
__eq__(self.other):equal to two object using the == operators
__lt__(self.other):less than two object using the < operators
__gt__(self.other):greater than two object using the > operators
'''

class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return vector(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return vector(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        return vector(self.a * other.a, self.b * other.b)
    def __truediv__(self, other):
        return vector(self.a / other.a, self.b / other.b)
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    def __repr__(self):
        return "vector({}, {})".format(self.a, self.b)
vector1=vector(1,2)
vector2=vector(3,4)
print(vector1+vector2)
print(vector1-vector2)
print(vector1*vector2)
print(vector1/vector2)


# overloading operator for complex Number

