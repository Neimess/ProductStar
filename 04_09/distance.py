from functools import total_ordering
from typing import Any

@total_ordering
class Millimeter:
    label = 'мм'
    ratio = 1 # Отношение определяемой еденицы измерения к миллиметрам

    def __init__(self, value) -> None:
      if isinstance(value, (int, float))  :
        self._value = value
      else:
        self._value = value.as_millimeters() / self.ratio
    
    def __repr__(self):
      return f"Inch({self._value})"

    def as_millimeters(self) -> float:
        """Возвращает значение длины в миллиметах.

        :rtype: float
        :return: Значение округленное до 5 знаков после запятой
        """
        return round(self._value * self.ratio, 5)
      
    def __add__(self, other):
      return type(self)(self._value + other.as_millimeters() / self.ratio)

    def __sub__(self, other):
      return type(self)(self._value - other.as_millimeters() / self.ratio)

    def __mul__(self, other):
      return type(self)(self._value * other.as_millimeters() / self.ratio)

    def __truediv__(self,other):
      return type(self)(self._value / other.as_millimeters() * self.ratio)

    def __eq__(self,other):
      return (hash(self) == hash(other.as_millimeters() / other.ratio))
    
    def __le__(self, other):
      return (self._value <= (other.as_millimeters() / self.ratio))

    def __hash__(self):
      return hash(self.as_millimeters())

    def test(self, other):
        print(self.as_millimeters())
        print(hash(self))
        print(hash(other.as_millimeters() / self.ratio))
        print((other.as_millimeters() / self.ratio))
class Centimeter(Millimeter):
    label = 'см'
    ratio = 10


class Meter(Millimeter):
    label = 'метр'
    ratio = 1000


class Inch(Millimeter):
    label = 'дюйм'
    ratio = 25.4
    

left = Millimeter(20.64)
right = Meter(0.02064)
print(right.as_millimeters())
print(left == right)
