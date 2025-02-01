from math import acos

# Vector4Int Class
class Vector4Int:
    def __init__(self, x : int, y : int, z : int, w : int):
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise TypeError(f"x must be an int or float, not {type(x).__name__}")
        if not isinstance(y, (int, float)) or isinstance(y, bool):
            raise TypeError(f"y must be an int or float, not {type(y).__name__}")
        if not isinstance(z, (int, float)) or isinstance(z, bool):
            raise TypeError(f"z must be an int or float, not {type(z).__name__}")
        if not isinstance(w, (int, float)) or isinstance(w, bool):
            raise TypeError(f"w must be an int or float, not {type(w).__name__}")

        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.w = int(w)



    # Regular Instance Methods:
    def magnitude(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w) ** 0.5

    def Normalize(self):
        self //= self.magnitude()


    def Normalized(self):
        return self // self.magnitude()



    # Static Methods
    @staticmethod
    def Dot(a : "Vector4Int", b : "Vector4Int") -> float:
        if not isinstance(a, Vector4Int) or not isinstance(b, Vector4Int):
            raise TypeError("Both Arguments Must Be Of Type Vector4Int.")

        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    @staticmethod
    def Distance(a : "Vector4Int", b : "Vector4Int") -> float:
        if not isinstance(a, Vector4Int) or not isinstance(b, Vector4Int):
            raise TypeError("Both Arguments Must Be Of Type Vector4Int.")

        return (a - b).magnitude()

    @staticmethod
    def Max(a : "Vector4Int", b : "Vector4Int"):
        if not isinstance(a, Vector4Int) or not isinstance(b, Vector4Int):
            raise TypeError("Both Arguments Must Be Of Type Vector4.")

        return Vector4Int(max(a.x, b.x), max(a.y, b.y), max(a.z, b.z), max(a.w, b.w))

    @staticmethod
    def Min(a : "Vector4Int", b : "Vector4Int"):
        if not isinstance(a, Vector4Int) or not isinstance(b, Vector4Int):
            raise TypeError("Both Arguments Must Be Of Type Vector4Int.")

        return Vector4Int(min(a.x, b.x), min(a.y, b.y), min(a.z, b.z), min(a.w, b.w))
    
    @staticmethod
    def Angle(a : "Vector4Int", b : "Vector4Int") -> float:
        if not isinstance(a, Vector4Int) or not isinstance(b, Vector4Int):
            raise TypeError("Both Arguments Must Be Of Type Vector4Int.")

        dot_product = Vector4Int.Dot(a, b)
        magnitude_product = a.magnitude() * b.magnitude()
        
        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(cos_theta) 


    @staticmethod
    def zero(): return Vector4Int(0, 0, 0, 0)
    @staticmethod
    def one(): return Vector4Int(1, 1, 1, 1)


    # Operators
    def __add__(self, o : "Vector4Int"):
        if not isinstance(o, Vector4Int):
            raise TypeError("Can Only Add With Type Vector4Int.")

        return Vector4Int(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o : "Vector4Int"):
        if not isinstance(o, Vector4Int):
            raise TypeError("Can Only Subtruct With Type Vector4Int.")

        return Vector4Int(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)

    def __mul__(self, o):
        return Vector4Int(self.x * o, self.y * o, self.z * o, self.w * o)

    def __truediv__(self, o : float):
        return Vector4Int(self.x // o, self.y // o, self.z // o, self.w // o)
    
    def floordiv(self, o : float):
        return self / o

    def __iadd__(self, o : "Vector4Int"):
        if not isinstance(o, Vector4Int):
            raise TypeError("Can Only Add With Type Vector4Int.")

        self.x += o.x
        self.y += o.y
        self.z += o.z
        self.w += o.w
        return self

    def __isub__(self, o : "Vector4Int"):
        if not isinstance(o, Vector4Int):
            raise TypeError("Can Only Subtruct With Type Vector4Int.")

        self.x -= o.x
        self.y -= o.y
        self.z -= o.z
        self.w -= o.w
        return self

    def __imul__(self, o):
        self.x *= o
        self.y *= o
        self.z *= o
        self.w *= o
        return self

    def __itruediv__(self, o):
        self.x //= o
        self.y //= o
        self.z //= o
        self.w //= o
        return self

    def __ifloordiv__(self, o : float):
        self /= o
        return self

    def __eq__(self, o : "Vector4Int"):
        if not isinstance(o, Vector4Int):
            raise TypeError("Can Only Compare With Type Vector4Int.")

        return self.x == o.x and self.y == o.y and self.z == o.z and self.w == o.w

    def __ne__(self, o : "Vector4Int"):
        if not isinstance(o, Vector4Int):
            raise TypeError("Can Only Compare With Type Vector4Int.")

        return self.x != o.x or self.y != o.y or self.z != o.z or self.w != o.w

    def __neg__(self):
        return Vector4Int(-self.x, -self.y, -self.z, -self.w)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z}, w={self.w})"
