class Chain:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        if isinstance(self.x, str):
            return repr((self.x + ' ').rstrip())
        elif isinstance(self.x, int):
            return repr(self.x)
        elif isinstance(self.x, float):
            if self.x.is_integer():
                return repr(int(self.x))
            else:
                return repr(self.x)

    def __eq__(self, x):
        if isinstance(x, str):
            return self.x == x
        elif isinstance(x, int):
            return self.x == x
        elif isinstance(x, float):
            return self.x == x
        return False

    def __call__(self, x):
        try:
            if isinstance(self.x, str):
                return Chain(self.x + ' ' + x)
            elif isinstance(self.x, int):
                return Chain(self.x + x)
            elif isinstance(self.x, float):
                return Chain(self.x + x)

        except TypeError:
            raise Exception('invalid operation')
# Examples

print(Chain(5)(6)(7))
print(Chain('Ali')('Safinal')('is')('the')('best.'))
print(Chain('abc')('defg') == 'abc defg')
print(Chain(64) == 64)
print(Chain(3)(1.5)(2)(3))
print(Chain(2.5)(2)(2)(2.5))
print(Chain('Ali')(5))