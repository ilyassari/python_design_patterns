class Product:
    def __init__(self):
        self.part1 = None
        self.part2 = None
        self.extras = []

    def __repr__(self):
        extras_str = ", ".join(self.extras)
        return f"Product({self.part1}, {self.part2}, Extras: {extras_str})"


class Builder:
    class Meta:
        abstract = True

    def build_part1(self):
        pass

    def build_part2(self):
        pass

    def add_extra(self):
        pass

    def get_result(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self, part1):
        self.product.part1 = part1

    def build_part2(self, part2):
        self.product.part2 = part2

    def add_extra(self, extra):
        self.product.extras.append(extra)

    def get_result(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, part1, part2, *extras):
        self.builder.build_part1(part1)
        self.builder.build_part2(part2)
        for extra in extras:
            self.builder.add_extra(extra)