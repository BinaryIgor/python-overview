from dataclasses import dataclass
from enum import Enum


class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'User({self.id}, {self.name})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        return isinstance(o, User) and self.id == o.id and self.name == o.name

    def __hash__(self):
        return hash(self.id) + 31 * hash(self.name)


@dataclass(frozen=True, unsafe_hash=True)
class ImmutableUser:
    id: int
    name: str


class Shape:

    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("Area method should be implemented!")


class Triangle(Shape):

    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def equilateral(a):
        return Triangle(a, a, a)

    def __str__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'

    def perimeter(self):
        return self._a + self._b + self._c


class Gender(Enum):
    MALE = 1,
    FEMALE = 2,
    OTHER = 3


u1 = User(1, "some user")
u2 = User(1, "some user")

if u1 == u2:
    print('u1 is equal to u2')

users_map = {u1: 'a', u2: 'b', User(2, 'another user'): 'c'}
print(f'Users map: {users_map}')

users_set = {u1, u2, User(3, 'different user')}
print(f'Users set: {users_set}')
print()

print(f"Immutable user: {ImmutableUser(1, 'ala')}")

if ImmutableUser(1, 'ala') == ImmutableUser(1, 'ala'):
    print("equal immutable users")
print()

triangle = Triangle(1, 2, 2)
print(f'Triangle ({triangle}) perimeter: {triangle.perimeter()}')
print(f'Equilateral triangle: {Triangle.equilateral(2)}')
print()

print(f"All Gender enums: ({list(Gender)})")
