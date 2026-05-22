def multiply_by(n):
    def multiplier(x):
        return x * n
    return multiplier

double = multiply_by(2)
print(double(5))

