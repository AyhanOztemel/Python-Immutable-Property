from immutableDecarator import immutable_property

class Circle:
    def __init__(self, radius, x,y,z):
        self._radius = radius
        self._x = x
        self._y = y
        self.z = z

    @immutable_property
    def radius(self):
        return self._radius

    @immutable_property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    

# Test the implementation
c = Circle(10, 5,11,15)
print("c.radius-->",c.radius)  # Output: 10
print("c.x--->",c.x)           # Output: 5
print("c.y--->",c.y)           # Output: 11
print("c.z--->",c.z)           # Output: 15

#Example-1
try:
    c.radius = 15  # This should raise an exception
    print(c.radius)
except AttributeError as e:
    print(e)  # Output: Cannot be assigned immutable property 'radius'
    
#Example-2
try:
    c.x = 10  # This should raise an exception
    print(c.x)
except AttributeError as e:
    print(e)  # Output: Cannot be assigned immutable property 'x'
    
#Example-3 
try:
    c.y = 10  # This should raise an exception
    print("c.y--->",c.y)
except AttributeError as e:
    print(e)  # Output: 10
    
#Example-4
try:
    c.z = 20  # This should raise an exception
    print("c.z--->",c.z)
except AttributeError as e:
    print(e)  # Output: 20

#Example-5 
c = Circle(25,415,121,185)
print("c.radius-->",c.radius)  # Output: 25
print("c.x--->",c.x)           # Output: 415
print("c.y--->",c.y)           # Output: 121
print("c.z--->",c.z)           # Output: 185
