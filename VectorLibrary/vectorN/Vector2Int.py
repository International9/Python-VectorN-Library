from math import acos

# Vector2Int Class
class Vector2Int:
    def __init__(self, x : int, y : int):
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise TypeError(f"x must be an int or float, not {type(x).__name__}")
        if not isinstance(y, (int, float)) or isinstance(y, bool):
            raise TypeError(f"y must be an int or float, not {type(y).__name__}")
        
        self.x : int = int(x)
        self.y : int = int(y)



    # Regular Instance Methods:
    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y) ** 0.5

    def Normalize(self):
        mag = self.magnitude()
        self.x //= mag
        self.y //= mag

    def Normalized(self):
        mag = self.magnitude()
        return Vector2Int(self.x // mag, self.y // mag)



    # Static Methods
    @staticmethod
    def Dot(a : "Vector2Int", b : "Vector2Int") -> float:
        if not isinstance(a, Vector2Int) or not isinstance(b, Vector2Int):
            raise TypeError("Both Arguments Must Be Of Type Vector2Int.")

        return a.x * b.x + a.y * b.y

    @staticmethod
    def Distance(a : "Vector2Int", b : "Vector2Int") -> float:
        if not isinstance(a, Vector2Int) or not isinstance(b, Vector2Int):
            raise TypeError("Both Arguments Must Be Of Type Vector2Int.")

        return (a - b).magnitude()

    @staticmethod
    def Max(a : "Vector2Int", b : "Vector2Int"):
        if not isinstance(a, Vector2Int) or not isinstance(b, Vector2Int):
            raise TypeError("Both Arguments Must Be Of Type Vector2Int.")

        return Vector2Int(max(a.x, b.x), max(a.y, b.y))

    @staticmethod
    def Min(a : "Vector2Int", b : "Vector2Int"):
        if not isinstance(a, Vector2Int) or not isinstance(b, Vector2Int):
            raise TypeError("Both Arguments Must Be Of Type Vector2Int.")

        return Vector2Int(min(a.x, b.x), min(a.y, b.y))
    
    @staticmethod
    def Angle(a : "Vector2Int", b : "Vector2Int") -> float:
        if not isinstance(a, Vector2Int) or not isinstance(b, Vector2Int):
            raise TypeError("Both Arguments Must Be Of Type Vector2Int.")

        dot_product = Vector2Int.Dot(a, b)
        magnitude_product = a.magnitude() * b.magnitude()
        
        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(cos_theta)


    @staticmethod
    def zero(): return Vector2Int(0, 0)
    @staticmethod
    def one(): return Vector2Int(1, 1)
    @staticmethod
    def right(): return Vector2Int(1, 0)
    @staticmethod
    def left(): return Vector2Int(-1, 0)
    @staticmethod
    def up(): return Vector2Int(0, 1)
    @staticmethod
    def down(): return Vector2Int(0, -1)



    # Operators
    def __add__(self, o : "Vector2Int"):
        if not isinstance(o, Vector2Int):
            raise TypeError("Can Only Add With Type Vector2Int.")

        return Vector2Int(self.x + o.x, self.y + o.y)

    def __sub__(self, o : "Vector2Int"):
        if not isinstance(o, Vector2Int):
            raise TypeError("Can Only Subtruct With Type Vector2Int.")

        return Vector2Int(self.x - o.x, self.y - o.y)

    def __mul__(self, o : float):
        return Vector2Int(int(self.x * o), int(self.y * o))

    def __truediv__(self, o : float):
        return Vector2Int(self.x // o, self.y // o)
    
    def __floordiv__(self, o : float):
        return self / o

    def __iadd__(self, o : "Vector2Int"):
        if not isinstance(o, Vector2Int):
            raise TypeError("Can Only Add With Type Vector2Int.")
            
        self.x += o.x
        self.y += o.y
        return self

    def __isub__(self, o : "Vector2Int"):
        if not isinstance(o, Vector2Int):
            raise TypeError("Can Only Subtruct With Type Vector2Int.")

        self.x -= o.x
        self.y -= o.y
        return self

    def __imul__(self, o : float):
        self.x *= int(o)
        self.y *= int(o)
        return self

    def __itruediv__(self, o : float):
        self.x //= o
        self.y //= o
        return self

    def __ifloordiv__(self, o : float):
        self /= o
        return self

    def __eq__(self, o : "Vector2Int"):
        if not isinstance(o, Vector2Int):
            raise TypeError("Can Only Compare With Type Vector2Int.")

        return self.x == o.x and self.y == o.y

    def __ne__(self, o : "Vector2Int"):
        if not isinstance(o, Vector2Int):
            raise TypeError("Can Only Compare With Type Vector2Int.")

        return self.x != o.x or self.y != o.y
    
    def __neg__(self):
        return Vector2Int(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"
