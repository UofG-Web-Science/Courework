from enum import Enum, auto


class Type(Enum):
    A = 1
    B = 2


type = Type.A

match type:
    case Type.A:
        print("A")
    case Type.B:
        print("B")
