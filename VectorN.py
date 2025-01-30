from math import acos

# Vector2 Class
class Vector2:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y



    # Regular Instance Methods:
    def magnitude(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def Normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    def Normalized(self):
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag)



    # Static Methods
    @staticmethod
    def Dot(a, b) -> float:
        return a.x * b.x + a.y * b.y

    @staticmethod
    def Distance(a, b) -> float:
        return (a - b).magnitude()

    @staticmethod
    def Max(a, b):
        x = y = 0
        
        if a.x > b.x:
            x = a.x
        else:
            x = b.x

        if a.y > b.y:
            y = a.y
        else:
            y = b.y

        return Vector2(x, y)

    @staticmethod
    def Min(a, b):
        x = y = 0
        
        if a.x < b.x:
            x = a.x
        else:
            x = b.x

        if a.y < b.y:
            y = a.y
        else:
            y = b.y

        return Vector2(x, y)
    
    @staticmethod
    def angle_between(self, other) -> float:
        dot_product = self.dot(other)
        magnitude_product = self.magnitude() * other.magnitude()

        if magnitude_product == 0:
            return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(max(-1, min(1, cos_theta))) 

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
    def __add__(self, o):
        return Vector2(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector2(self.x - o.x, self.y - o.y)

    def __mul__(self, o):
        return Vector2(self.x * o, self.y * o)

    def __truediv__(self, o):
        return Vector2(self.x / o, self.y / o)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        return self

    def __isub__(self, o):
        self.x -= o.x
        self.y -= o.y
        return self

    def __imul__(self, o):
        self.x *= o
        self.y *= o
        return self

    def __itruediv__(self, o):
        self.x /= o
        self.y /= o
        return self

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"

# Vector2Int Class
class Vector2Int:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y



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
    def Dot(a, b) -> float:
        return a.x * b.x + a.y * b.y

    @staticmethod
    def Distance(a, b) -> float:
        return (a - b).magnitude()

    @staticmethod
    def Max(a, b):
        x = y = 0
        
        if a.x > b.x:
            x = a.x
        else:
            x = b.x

        if a.y > b.y:
            y = a.y
        else:
            y = b.y

        return Vector2Int(x, y)

    @staticmethod
    def Min(a, b):
        x = y = 0
        
        if a.x < b.x:
            x = a.x
        else:
            x = b.x

        if a.y < b.y:
            y = a.y
        else:
            y = b.y

        return Vector2Int(x, y)
    
    @staticmethod
    def angle_between(self, other) -> float:
        dot_product = self.dot(other)
        magnitude_product = self.magnitude() * other.magnitude()
        
        if magnitude_product == 0:
            return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(max(-1, min(1, cos_theta))) 


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
    def __add__(self, o):
        return Vector2Int(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector2Int(self.x - o.x, self.y - o.y)

    def __mul__(self, o):
        return Vector2Int(self.x * o, self.y * o)

    def __truediv__(self, o):
        return Vector2Int(self.x // o, self.y // o)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        return self

    def __isub__(self, o):
        self.x -= o.x
        self.y -= o.y
        return self

    def __imul__(self, o):
        self.x *= o
        self.y *= o
        return self

    def __itruediv__(self, o):
        self.x //= o
        self.y //= o
        return self

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __neg__(self):
        return Vector2Int(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"

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
    def Dot(a, b) -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def Distance(a, b) -> float:
        return (a - b).magnitude()

    @staticmethod
    def Max(a, b):
        x = y = z = 0
        
        if a.x > b.x:
            x = a.x
        else:
            x = b.x

        if a.y > b.y:
            y = a.y
        else:
            y = b.y

        if a.z > b.z:
            z = a.z
        else:
            z = b.z

        return Vector3(x, y, z)

    @staticmethod
    def Min(a, b):
        x = y = z = 0
        
        if a.x < b.x:
            x = a.x
        else:
            x = b.x

        if a.y < b.y:
            y = a.y
        else:
            y = b.y

        if a.z < b.z:
            z = a.z
        else:
            z = b.z

        return Vector3(x, y, z)
    
    @staticmethod
    def angle_between(self, other) -> float:
        dot_product = self.dot(other)
        magnitude_product = self.magnitude() * other.magnitude()
        
        if magnitude_product == 0:
            return 0
        
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
    def __add__(self, o):
        return Vector3(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return Vector3(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o):
        return Vector3(self.x * o, self.y * o, self.z * o)

    def __truediv__(self, o):
        return Vector3(self.x / o, self.y / o, self.z / o)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        self.z += o.z
        return self

    def __isub__(self, o):
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

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.z == o.z

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z})"

# Vector3Int Class
class Vector3Int:
    def __init__(self, x : int, y : int, z : int):
        self.x = x
        self.y = y
        self.z = z



    # Regular Instance Methods:
    def magnitude(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

    def Normalize(self):
        mag = self.magnitude()
        self.x //= mag
        self.y //= mag
        self.z //= mag

    def Normalized(self):
        mag = self.magnitude()
        return Vector3Int(self.x // mag, self.y // mag, self.z // mag)



    # Static Methods
    @staticmethod
    def Dot(a, b) -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def Distance(a, b) -> float:
        return (a - b).magnitude()

    @staticmethod
    def Max(a, b):
        x = y = z = 0
        
        if a.x > b.x:
            x = a.x
        else:
            x = b.x

        if a.y > b.y:
            y = a.y
        else:
            y = b.y

        if a.z > b.z:
            z = a.z
        else:
            z = b.z

        return Vector3Int(x, y, z)

    @staticmethod
    def Min(a, b):
        x = y = z = 0
        
        if a.x < b.x:
            x = a.x
        else:
            x = b.x

        if a.y < b.y:
            y = a.y
        else:
            y = b.y

        if a.z < b.z:
            z = a.z
        else:
            z = b.z

        return Vector3Int(x, y, z)
    
    @staticmethod
    def angle_between(self, other) -> float:
        dot_product = self.dot(other)
        magnitude_product = self.magnitude() * other.magnitude()
        
        if magnitude_product == 0:
            return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(max(-1, min(1, cos_theta))) 


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
    def __add__(self, o):
        return Vector3Int(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return Vector3Int(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, o):
        return Vector3Int(self.x * o, self.y * o, self.z * o)

    def __truediv__(self, o):
        return Vector3Int(self.x // o, self.y // o, self.z // o)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        self.z += o.z
        return self

    def __isub__(self, o):
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
        self.x //= o
        self.y //= o
        self.z //= o
        return self

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.z == o.z

    def __neg__(self):
        return Vector3Int(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z})"

# Vector4 Class
class Vector4:
    def __init__(self, x : float, y : float, z : float, w : float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w



    # Regular Instance Methods:
    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w) ** 0.5

    def Normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag
        self.z /= mag
        self.w /= mag

    def Normalized(self):
        mag = self.magnitude()
        return Vector4(self.x / mag, self.y / mag, self.z / mag, self.w / mag)



    # Static Methods
    @staticmethod
    def Dot(a, b) -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    @staticmethod
    def Distance(a, b) -> float:
        return (a - b).magnitude()

    @staticmethod
    def Max(a, b):
        x = y = z = w = 0
        
        if a.x > b.x:
            x = a.x
        else:
            x = b.x

        if a.y > b.y:
            y = a.y
        else:
            y = b.y

        if a.z > b.z:
            z = a.z
        else:
            z = b.z

        if a.w > b.w:
            w = a.w
        else:
            w = b.w

        return Vector4(x, y, z, w)

    @staticmethod
    def Min(a, b):
        x = y = z = w = 0
        
        if a.x < b.x:
            x = a.x
        else:
            x = b.x

        if a.y < b.y:
            y = a.y
        else:
            y = b.y

        if a.z < b.z:
            z = a.z
        else:
            z = b.z

        if a.w < b.w:
            w = a.w
        else:
            w = b.w

        return Vector4(x, y, z, w)
    
    @staticmethod
    def angle_between(self, other) -> float:
        dot_product = self.dot(other)
        magnitude_product = self.magnitude() * other.magnitude()
        
        if magnitude_product == 0:
            return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(max(-1, min(1, cos_theta))) 


    @staticmethod
    def zero(): return Vector4(0, 0, 0, 0)
    @staticmethod
    def one(): return Vector4(1, 1, 1, 1)



    # Operators
    def __add__(self, o):
        return Vector4(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o):
        return Vector4(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)

    def __mul__(self, o):
        return Vector4(self.x * o, self.y * o, self.z * o, self.w * o)

    def __truediv__(self, o):
        return Vector4(self.x / o, self.y / o, self.z / o, self.w / o)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        self.z += o.z
        self.w += o.w
        return self

    def __isub__(self, o):
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
        self.x /= o
        self.y /= o
        self.z /= o
        self.w /= o
        return self

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.z == o.z and self.w == o.w

    def __neg__(self):
        return Vector4(-self.x, -self.y, -self.z, -self.w)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z}, w={self.w})"

# Vector4Int Class
class Vector4Int:
    def __init__(self, x : int, y : int, z : int, w : int):
        self.x = x
        self.y = y
        self.z = z
        self.w = w



    # Regular Instance Methods:
    def magnitude(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w) ** 0.5

    def Normalize(self):
        mag = self.magnitude()
        self.x //= mag
        self.y //= mag
        self.z //= mag

    def Normalized(self):
        mag = self.magnitude()
        return Vector4Int(self.x // mag, self.y // mag, self.z // mag, self.w // mag)



    # Static Methods
    @staticmethod
    def Dot(a, b) -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    @staticmethod
    def Distance(a, b) -> float:
        return (a - b).magnitude()

    @staticmethod
    def Max(a, b):
        x = y = z = w = 0
        
        if a.x > b.x:
            x = a.x
        else:
            x = b.x

        if a.y > b.y:
            y = a.y
        else:
            y = b.y

        if a.z > b.z:
            z = a.z
        else:
            z = b.z
        
        if a.w > b.w:
            w = a.w
        else:
            w = b.w


        return Vector4Int(x, y, z, w)

    @staticmethod
    def Min(a, b):
        x = y = z = 0
        
        if a.x < b.x:
            x = a.x
        else:
            x = b.x

        if a.y < b.y:
            y = a.y
        else:
            y = b.y

        if a.z < b.z:
            z = a.z
        else:
            z = b.z

        if a.w < b.w:
            w = a.w
        else:
            w = b.w

        return Vector4Int(x, y, z, w)
    
    @staticmethod
    def angle_between(self, other) -> float:
        dot_product = self.dot(other)
        magnitude_product = self.magnitude() * other.magnitude()
        
        if magnitude_product == 0:
            return 0
        
        cos_theta = dot_product / magnitude_product
        return acos(max(-1, min(1, cos_theta))) 


    @staticmethod
    def zero(): return Vector4Int(0, 0, 0, 0)
    @staticmethod
    def one(): return Vector4Int(1, 1, 1, 1)


    # Operators
    def __add__(self, o):
        return Vector4Int(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o):
        return Vector4Int(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)

    def __mul__(self, o):
        return Vector4Int(self.x * o, self.y * o, self.z * o, self.w * o)

    def __truediv__(self, o):
        return Vector4Int(self.x // o, self.y // o, self.z // o, self.w // o)

    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        self.z += o.z
        self.w += o.w
        return self

    def __isub__(self, o):
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

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y and self.z == o.z and self.w == o.w

    def __neg__(self):
        return Vector4Int(-self.x, -self.y, -self.z, -self.w)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y}, z={self.z}, w={self.w})"
