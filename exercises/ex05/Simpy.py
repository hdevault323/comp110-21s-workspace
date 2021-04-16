"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730236759"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes the values attribute of the simpy object."""
        self.values = values 

    def __repr__(self) -> str: 
        """Magic method to represent object as a string."""
        return f"Simpy({self.values})"

    def fill(self, fillers: float, x: int) -> None: 
        """Fills simpy's values with n number of repeating values."""
        list_values: list[float] = []
        i = 0
        while i < x:
            list_values.append(fillers)
            i += 1
        self.values = list_values

    def arange(self, start: float, stop: float, step = 1.0) -> None:
        """Fills in the values attribute with a range of values."""
        step != 0.0
        list_values: list[float] = []
        i: float = start 
        if i < stop:
            while i < stop:
                list_values.append(i)
                i += float(step)
        else: 
            if i > stop: 
                while i > stop:
                    list_values.append(i)
                    i += float(step)
        self.values = list_values

    def sum(self) -> float: 
        """Takes the sum of values."""
        summable: list[float] = []
        summable = self.values
        total: float = 0.0
        for i in range(0, len(summable), 1):
            total += summable[i]
            i += 1
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading the addition operator for Simpy and float."""
        added: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                added.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)): 
                added.append(self.values[i] + rhs.values[i])
        return Simpy(added)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading the power operator for Simpy and float."""
        exponential: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                exponential.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)): 
                exponential.append(self.values[i] ** rhs.values[i])
        return Simpy(exponential)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading the item-wise operator for Simpy and float."""
        remainder: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                remainder.append(item % rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)): 
                remainder.append(self.values[i] % rhs.values[i])
        return Simpy(remainder)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading the == for float and Simpy."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)): 
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloadinf the > operator for float and Simpy."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)): 
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows subscription notation with Simpy."""
        if isinstance(rhs, int):
            number = float
            number = self.values[rhs]
            return number
        else: 
            assert len(self.values) == len(rhs)
            result: list[bool] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
        return Simpy(result)