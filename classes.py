#import temp.test


class Club:
    T = ("one", "two")

    def __init__(self, name, players=[]):
        self.name = name
        self.players = players

    # optional
    def __len__(self):
        return len(self.players)

    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]
    def __getitem__(self, i):
        return self.players[i]

    # Note: len and getitem function make class object iterable using for loop

    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    def __repr__(self):
        return f"Club {self.name}: {self.players}"

    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    def __str__(self):
        return f"Club {self.name} with {len(self)} players"

    # @property for using function as property

    @classmethod
    def clsFunc(cls):
        print('clas method', cls, cls.T)

    @staticmethod
    def static():
        print("Static func")


cl = Club("aa")
Club.clsFunc()
cl.players.append("ZZ")
cl.players.append("P2")
for i in cl:
    print(i)

# print(__name__)


# Multiple inheritance
class Salary:
    def calculate(self, hours: float) -> float:
        return self.rate * hours


class Promotable:
    # _raise so it doesn't clash with Python's raise keyword!
    def promote(self, _raise: float) -> None:
        self.rate += _raise


class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)


e = Employee(10)
print(e.weekly_salary())
e.promote(22)
print(e.weekly_salary())
