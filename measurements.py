from expression import Expression


class Gallons(Expression):

    def gallons(self, q: float) -> str:
        return str(q)

    def quarts(self, q: float) -> str:
        return str(q * 4)

    def pints(self, q: float) -> str:
        return str(q * 8)

    def cups(self, q: float) -> str:
        return str(q * 16)

    def tablespoons(self, q: float) -> str:
        return str(q * 256)


class Pints(Expression):

    def gallons(self, q: float) -> str:
        return str(q / 8)

    def quarts(self, q: float) -> str:
        return str(q / 2)

    def pints(self, q: float) -> str:
        return str(q)

    def cups(self, q: float) -> str:
        return str(q * 2)

    def tablespoons(self, q: float) -> str:
        return str(q * 32)


class Quarts(Expression):

    def gallons(self, q: float) -> str:
        return str(q / 4)

    def quarts(self, q: float) -> str:
        return str(q)

    def pints(self, q: float) -> str:
        return str(q * 2)

    def cups(self, q: float) -> str:
        return str(q * 4)

    def tablespoons(self, q: float) -> str:
        return str(q * 64)


class Cups(Expression):

    def gallons(self, q: float) -> str:
        return str(q / 16)

    def quarts(self, q: float) -> str:
        return str(q / 4)

    def pints(self, q: float) -> str:
        return str(q / 2)

    def cups(self, q: float) -> str:
        return str(q)

    def tablespoons(self, q: float) -> str:
        return str(q * 16)


class Tablespoons(Expression):

    def gallons(self, q: float) -> str:
        return str(q / 256)

    def quarts(self, q: float) -> str:
        return str(q / 64)

    def pints(self, q: float) -> str:
        return str(q / 32)

    def cups(self, q: float) -> str:
        return str(q / 16)

    def tablespoons(self, q: float) -> str:
        return str(q)
