from math import acos

# Vector3Int Class
class Vector3Int:
    def __init__(self, x : int, y : int, z : int):
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise TypeError(f"x must be an int or float, not {type(x).__name__}")
        if not isinstance(y, (int, float)) or isinstance(y, bool):
            raise TypeError(f"y must be an int or float, not {type(y).__name__}")
        if not isinstance(z, (int, float)) or isinstance(z, bool):
            raise TypeError(f"z must be an int or float, not {type(z).__name__}")

        self.x = int(x)
        self.y = int(y)
        self.z = int(z)



    # Regular Instance Methods:
    def magnitude(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

    def Normalize(self):
        self.x //= self.magnitude()

    def Normalized(self):
        return self // self.magnitude()



    # Static Methods
    @staticmethod
    def Dot(a : "Vector3Int", b : "Vector3Int") -> float:
        if not isinstance(a, Vector3Int) or not isinstance(b, Vector3Int):
            raise TypeError("Both Arguments Must Be Of Type Vector3Int.")

        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def Distance(a : "Vector3Int", b : "Vector3Int") -> float:
        if not isinstance(a, Vector3Int) or not isinstance(b, Vector3Int):
            raise TypeError("Both Arguments Must Be Of Type Vector3Int.")

        return (a - b).magnitude()


    @staticmethod
    def Max(a : "Vector3Int", b : "Vector3Int"):
        if not isinstance(a, Vector3Int) or not isinstance(b, Vector3Int):
            raise TypeError("Both Arguments Must Be Of Type Vector3Int.")

        return Vector3Int(min(a.x, b.x), min(a.y, b.y), min(a.z, b.z))

    @staticmethod
    def Min(a : "Vector3Int", b : "Vector3Int"):
        if not isinstance(a, Vector3Int) or not isinstance(b, Vector3Int):
            raise TypeError("Both Arguments Must Be Of Type Vector3Int.")
        
        return Vector3Int(max(a.x, b.x), max(a.y, b.y), max(a.z, b.z))
    
    
    @staticmethod
    def Angle(a : "Vector3Int", b : "Vector3Int") -> float:
        if not isinstance(a, Vector3Int) or not isinstance(b, Vector3Int):
            raise TypeError("Both Arguments Must Be Of Type Vector3Int.")

        dot_product = Vector3Int.Dot(a, b)
        magnitude_product = a.magnitude() * b.magnitude()
        
        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(cos_theta)
    

    @staticmethod
    def zero(): return Vector3Int(0, 0, 0)
    @staticmethod
    def one(): return Vector3Int(1, 1, 1)
    @staticmethod
    def right(): return Vector3Int(1, 0, 0)
    @staticmethod
    def left(): return Vector3Int(-1, 0, 0)
    @staticmethod
    def up(): return Vector3Int(0, 1, 0)
    @staticmethod
    def down(): return Vector3Int(0, -1, 0)
    @staticmethod
    def back(): return Vector3Int(0, 0, -1)
    @staticmethod
    def forward(): return Vector3Int(0, 0, 1)



    # Operators
    def __add__(self, o : "Vector3Int"):
        if not isinstance(o, Vector3Int):
            raise TypeError("Can Only Add With Type Vector3Int.")

        return Vector3Int(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o : "Vector3Int"):
        if not isinstance(o, Vector3Int):
            raise TypeError("Can Only Subtruct With Type Vector3Int.")

        return Vector3Int(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o):
        return Vector3Int(self.x * o, self.y * o, self.z * o)

    def __truediv__(self, o):
        return Vector3Int(self.x // o, self.y // o, self.z // o)

    def __floordiv__(self, o : float):
        return self / o

    def __iadd__(self, o : "Vector3Int"):
        if not isinstance(o, Vector3Int):
            raise TypeError("Can Only Add With Type Vector3Int.")

        self.x += o.x
        self.y += o.y
        self.z += o.z
        return self

    def __isub__(self, o : "Vector3Int"):
        if not isinstance(o, Vector3Int):
            raise TypeError("Can Only Subtruct With Type Vector3Int.")

        self.x -= o.x
        self.y -= o.y
        self.z -= o.z
        return self

    def __imul__(self, o):
        self.x *= o
        self.y *= o
        self.z *= o
        return self

    def __itruediv__(self, o : float):
        self.x //= o
        self.y //= o
        self.z //= o
        return self

    def __ifloordiv__(self, o : float):
        self /= o
        return self

    def __eq__(self, o : "Vector3Int"):
        if not isinstance(o, Vector3Int):
            raise TypeError("Can Only Compare With Type Vector3Int.")

        return self.x == o.x and self.y == o.y and self.z == o.z

    def __ne__(self, o : "Vector3Int"):
        if not isinstance(o, Vector3Int):
            raise TypeError("Can Only Compare With Type Vector3Int.")

        return self.x != o.x or self.y != o.y or self.z != o.z

    def __neg__(self):
        return Vector3Int(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z})"
