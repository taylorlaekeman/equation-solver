from abc import ABC as AbstractBaseClass, abstractmethod


def get_equation_solver(equation):
    if '*' in equation:
        return Multiplier(equation)
    elif '/' in equation:
        return Divider(equation)
    elif '+' in equation:
        return Adder(equation)
    else:
        return Subtractor(equation)


class EquationSolver(AbstractBaseClass):
    def __init__(self, equation):
        operator = self.get_operator()
        [lhs, rhs] = equation.split(operator)
        self.lhs = int(lhs)
        self.rhs = int(rhs)

    @abstractmethod
    def get_operator(self):
        pass

    @abstractmethod
    def solve(self):
        pass


class Multiplier(EquationSolver):
    def get_operator(self):
        return '*'

    def solve(self):
        return self.lhs * self.rhs


class Divider(EquationSolver):
    def get_operator(self):
        return '/'

    def solve(self):
        return self.lhs / self.rhs


class Adder(EquationSolver):
    def get_operator(self):
        return '+'

    def solve(self):
        return self.lhs + self.rhs


class Subtractor(EquationSolver):
    def get_operator(self):
        return '-'

    def solve(self):
        return self.lhs - self.rhs
