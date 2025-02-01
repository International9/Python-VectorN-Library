from math import acos

# Vector2 Class
class Vector2:
    def __init__(self, x : float, y : float):      
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise TypeError(f"x must be an int or float, not {type(x).__name__}")
        if not isinstance(y, (int, float)) or isinstance(y, bool):
            raise TypeError(f"y must be an int or float, not {type(y).__name__}")
          
        self.x = x
        self.y = y



    # Regular Instance Methods:
    def magnitude(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def Normalize(self):
        self /= self.magnitude()

    def Normalized(self):
        return self / self.magnitude()


    # Static Methods
    @staticmethod
    def Dot(a : "Vector2", b : "Vector2") -> float:
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return a.x * b.x + a.y * b.y

    @staticmethod
    def Distance(a : "Vector2", b : "Vector2") -> float:
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return (a - b).magnitude()

    @staticmethod
    def Max(a : "Vector2", b : "Vector2"):
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return Vector2(max(a.x, b.x), max(a.y, b.y))

    @staticmethod
    def Min(a : "Vector2", b : "Vector2"):
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")

        return Vector2(min(a.x, b.x), min(a.y, b.y))
    
    @staticmethod
    def Angle(a : "Vector2", b : "Vector2") -> float:
        if not isinstance(a, Vector2) or not isinstance(b, Vector2):
            raise TypeError("Both Arguments Must Be Of Type Vector2.")
            
        dot_product = Vector2.Dot(a, b)
        magnitude_product = a.magnitude() * b.magnitude()

        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(cos_theta)

    @staticmethod
    def zero(): return Vector2(0, 0)
    @staticmethod
    def one(): return Vector2(1, 1)
    @staticmethod
    def right(): return Vector2(1, 0)
    @staticmethod
    def left(): return Vector2(-1, 0)
    @staticmethod
    def up(): return Vector2(0, 1)
    @staticmethod
    def down(): return Vector2(0, -1)



    # Operators
    def __add__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Add With Type Vector2.")

        return Vector2(self.x + o.x, self.y + o.y)

    def __sub__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Subtruct With Type Vector2.")

        return Vector2(self.x - o.x, self.y - o.y)

    def __mul__(self, o : float):
        return Vector2(self.x * o, self.y * o)

    def __truediv__(self, o : float):
        return Vector2(self.x / o, self.y / o)

    def __floordiv__(self, o : float):
        return Vector2(self.x // o, self.y // o)

    def __iadd__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Add With Type Vector2.")

        self.x += o.x
        self.y += o.y
        return self

    def __isub__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Subtruct With Type Vector2.")

        self.x -= o.x
        self.y -= o.y
        return self

    def __imul__(self, o : float):
        self.x *= o
        self.y *= o
        return self

    def __itruediv__(self, o : float):
        self.x /= o
        self.y /= o
        return self
    
    def __ifloordiv__(self, o : float):
        self.x //= o
        self.y //= o
        return self

    def __eq__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Compare With Type Vector2.")

        return self.x == o.x and self.y == o.y
    
    def __ne__(self, o : "Vector2"):
        if not isinstance(o, Vector2):
            raise TypeError("Can Only Compare With Type Vector2.")

        return (self.x != o.x) or (self.y != o.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"
