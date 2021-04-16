"""Examples of object-oriented programming concepts."""

from __future__ import annotations

 class Point:

    # defining attributes (related variables)
    # of our class.
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y arguments."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """MAgic method to represent object as a string."""
        return f"{self.x}, {self.y}"

    def scale_by(self, factor: float) -> None:
        self.x *= factor
        self.y *= factor

    def scale (self, factor: float) -> Point:
        """Scale a Point's attributes by factor."""
        return Point(self.x * factor, self.y * factor)

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        print("__mul__ was called")
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        """Overloading the addition operator for Point * float."""
        return Point(self.x + rhs, self.y + rhs.y)

    def __getitem__(self,, index: int) -> float:
        """Overload the subscriptrion notation."""
        if index == 0: 
            return self x
        elif index == 1:
            return self y
        elif:
            raise IndexError

    
a: Point = Point(1.0, 2.0)
b: Point = a * 2.0 # need to add specail method for this to work
c: Point = a + b 
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

3
print(a[0])
print(a[1])