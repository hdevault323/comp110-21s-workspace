"""Examples of Vectorized operations on strarray."""

from __future__ import annotations


class StrArray:
    """Utility class for common string column operations."""

    values: list[str]

    def __init__(self, values: list[str]):
        """Initializes the constructor call."""
        self.values = values
    
    def __repr__(self) -> str:
        """Represents the StrArray as a str."""
        return f"StrArray({self.values})"
    
    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return StrArray(result)


s: StrArray = StrArray(["a", "b", "c"])
t = StrArray(["d", "e", "f"])
print(s + "wow")
print(s + t)

first = StrArray(["Kris", "Kaki", "Michael"])
last = StrArray(["Jordan", "Ryan", "Jordan"])
full_name = last + ", " + first
print(full_name)
