"""Examplesz of optional parameters and union types."""

from typing import Union

def hello(name: Union[str, int] = "World") -> str:
  """A greeting."""
  greeting: str = "hello "
  if isinstance(name, str):
      greeting += name
  return greeting


#single-argument
print(hello("Sally"))

#no argument
print(hello())

#int argument works too
print(hello(110))


def add(lhs: float = 0.0, rhs: Union[str, float] = 0.0) -> float:
    result: float = lhs
    if isinstance(rhs, str):
        result += float(rhs)
    else:
        result += rhs
    return result



print(add(110.0, "100.0"))