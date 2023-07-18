import copy

class Prototype:
    class Meta:
        abstract = True

    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    property1 = 0
    property2 = 0
    property3 = 0

    