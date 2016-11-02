import collections

__logmodule__ = True


# class A(collections.namedtuple("A", "x y")):

#     def sum(self):
#         return self.x + self.y


class B():

    def __init__(self):
        self.x = 1
        print('Class B initialized')


class B1(B):

    def cosa(self):
        return self.x + 1


class Base():

    def __init__(self, c):
        print('original')


class Derived(Base):

    def __init__(self, b, c, x):
        print('derived')
        super().__init__(c)


class Subclass(Derived):
    pass


class Subsubclass(Subclass):
    pass
