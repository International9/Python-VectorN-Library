from math import acos

# Vector4 Class
class Vector4:
    def __init__(self, x : float, y : float, z : float, w : float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w





    # Setters:
    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set X To That Type! Only Int Or Float.")
        
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set Y To That Type! Only Int Or Float.")
        
        self._y = value

    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set Z To That Type! Only Int Or Float.")
        
        self._z = value

    @property
    def w(self) -> float:
        return self._w
    
    @w.setter
    def w(self, value):
        if (not isinstance(value, (int, float)) or isinstance(value, bool)):
            raise TypeError("Cannot Set W To That Type! Only Int Or Float.")
        
        self._w = value






    @property
    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w) ** 0.5

    @property
    def Normalized(self):
        mag = self.magnitude
        return Vector4(self.x / mag, self.y / mag, self.z / mag, self.w / mag)

    # Regular Instance Methods:
    def Normalize(self):
        self.x /= self.magnitude



    # Static Methods
    @staticmethod
    def Dot(a : "Vector4", b : "Vector4") -> float:
        if not isinstance(a, Vector4) or not isinstance(b, Vector4):
            raise TypeError("Both Arguments Must Be Of Type Vector4.")

        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    @staticmethod
    def Distance(a : "Vector4", b : "Vector4") -> float:
        if not isinstance(a, Vector4) or not isinstance(b, Vector4):
            raise TypeError("Both Arguments Must Be Of Type Vector4.")

        return (a - b).magnitude

    @staticmethod
    def Max(a : "Vector4", b : "Vector4"):
        if not isinstance(a, Vector4) or not isinstance(b, Vector4):
            raise TypeError("Both Arguments Must Be Of Type Vector4.")

        return Vector4(max(a.x, b.x), max(a.y, b.y), max(a.z, b.z), max(a.w, b.w))

    @staticmethod
    def Min(a : "Vector4", b : "Vector4"):
        if not isinstance(a, Vector4) or not isinstance(b, Vector4):
            raise TypeError("Both Arguments Must Be Of Type Vector4.")

        return Vector4(min(a.x, b.x), min(a.y, b.y), min(a.z, b.z), min(a.w, b.w))

    
    @staticmethod
    def Angle(a : "Vector4", b : "Vector4") -> float:
        if not isinstance(a, Vector4) or not isinstance(b, Vector4):
            raise TypeError("Both Arguments Must Be Of Type Vector4.")

        dot_product = Vector4.Dot(a, b)
        magnitude_product = a.magnitude * b.magnitude
        
        if magnitude_product == 0: return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(cos_theta) 
    


    @staticmethod
    def zero(): return Vector4(0, 0, 0, 0)
    @staticmethod
    def one(): return Vector4(1, 1, 1, 1)



    # Operators
    def __add__(self, o : "Vector4"):
        if not isinstance(o, Vector4):
            raise TypeError("Can Only Add With Type Vector4.")

        return Vector4(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o : "Vector4"):
        if not isinstance(o, Vector4):
            raise TypeError("Can Only Subtruct With Type Vector4.")

        return Vector4(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)

    def __mul__(self, o):
        return Vector4(self.x * o, self.y * o, self.z * o, self.w * o)

    def __truediv__(self, o):
        return Vector4(self.x / o, self.y / o, self.z / o, self.w / o)
    
    def __floordiv__(self, o):
        return Vector4(self.x // o, self.y // o, self.z // o, self.w // o)

    def __iadd__(self, o : "Vector4"):
        if not isinstance(o, Vector4):
            raise TypeError("Can Only Add With Type Vector4.")

        self.x += o.x
        self.y += o.y
        self.z += o.z
        self.w += o.w
        return self

    def __isub__(self, o : "Vector4"):
        if not isinstance(o, Vector4):
            raise TypeError("Can Only Subtruct With Type Vector4.")

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

    def __itruediv__(self, o):
        self.x /= o
        self.y /= o
        self.z /= o
        self.w /= o
        return self
    
    def __ifloordiv__(self, o : float):
        self.x //= o
        self.y //= o
        self.z //= o
        self.w //= o
        return self

    def __eq__(self, o : "Vector4"):
        if not isinstance(o, Vector4):
            raise TypeError("Can Only Compare With Type Vector4.")

        return self.x == o.x and self.y == o.y and self.z == o.z and self.w == o.w

    def __ne__(self, o : "Vector4"):
        if not isinstance(o, Vector4):
            raise TypeError("Can Only Compare With Type Vector4.")

        return self.x != o.x or self.y != o.y or self.z != o.z or self.w != o.w

    def __neg__(self):
        return Vector4(-self.x, -self.y, -self.z, -self.w)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z}, w={self.w})"
