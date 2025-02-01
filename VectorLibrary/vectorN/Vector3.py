from math import acos

# Vector3 Class
class Vector3:
    def __init__(self, x : float, y : float, z : float):
        self.x = x
        self.y = y
        self.z = z



    # Regular Instance Methods:
    def magnitude(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

    def Normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag
        self.z /= mag

    def Normalized(self):
        mag = self.magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)



    # Static Methods
    @staticmethod
    def Dot(a : "Vector3", b : "Vector3") -> float:
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def Distance(a : "Vector3", b : "Vector3") -> float:
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        return (a - b).magnitude()

    @staticmethod
    def Max(a : "Vector3", b : "Vector3"):
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        return Vector3(min(a.x, b.x), min(a.y, b.y), min(a.z, b.z))

    @staticmethod
    def Min(a : "Vector3", b : "Vector3"):
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")
        
        return Vector3(max(a.x, b.x), max(a.y, b.y), max(a.z, b.z))
    
    @staticmethod
    def Angle(a : "Vector3", b : "Vector3") -> float:
        if not isinstance(a, Vector3) or not isinstance(b, Vector3):
            raise TypeError("Both Arguments Must Be Of Type Vector3.")

        dot_product = Vector3.Dot(a, b)
        magnitude_product = a.magnitude() * b.magnitude()
        
        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(max(-1, min(1, cos_theta))) 



    @staticmethod
    def zero(): return Vector3(0, 0, 0)
    @staticmethod
    def one(): return Vector3(1, 1, 1)
    @staticmethod
    def right(): return Vector3(1, 0, 0)
    @staticmethod
    def left(): return Vector3(-1, 0, 0)
    @staticmethod
    def up(): return Vector3(0, 1, 0)
    @staticmethod
    def down(): return Vector3(0, -1, 0)
    @staticmethod
    def back(): return Vector3(0, 0, -1)
    @staticmethod
    def forward(): return Vector3(0, 0, 1)



    # Operators
    def __add__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Add With Type Vector3.")

        return Vector3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Subtruct With Type Vector3.")

        return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o):
        return Vector3(self.x * o, self.y * o, self.z * o)

    def __truediv__(self, o):
        return Vector3(self.x / o, self.y / o, self.z / o)
    
    def __floordiv__(self, o : float):
        return Vector3(self.x // o, self.y // o, self.z // o)

    def __iadd__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Add With Type Vector3.")
            
        self.x += o.x
        self.y += o.y
        self.z += o.z
        return self

    def __isub__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Subtruct With Type Vector3.")

        self.x -= o.x
        self.y -= o.y
        self.z -= o.z
        return self

    def __imul__(self, o):
        self.x *= o
        self.y *= o
        self.z *= o
        return self

    def __itruediv__(self, o):
        self.x /= o
        self.y /= o
        self.z /= o
        return self

    def __ifloordiv__(self, o : float):
        self.x //= o
        self.y //= o
        self.z //= o
        return self

    def __eq__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Compare With Type Vector3.")

        return self.x == o.x and self.y == o.y and self.z == o.z
    
    def __ne__(self, o : "Vector3"):
        if not isinstance(o, Vector3):
            raise TypeError("Can Only Compare With Type Vector3.")

        return self.x != o.x or self.y != o.y or self.z != o.z

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z})"
