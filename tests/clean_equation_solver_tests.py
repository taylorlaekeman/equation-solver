from unittest import TestCase

from clean.equation_solver import get_equation_solver


class EquationSolverTests(TestCase):
    def test_addition(self):
        equation = "9+1"
        solver = get_equation_solver(equation)
        result = solver.solve()
        self.assertEquals(result, 10)

    def test_subtraction(self):
        equation = "92-4"
        solver = get_equation_solver(equation)
        result = solver.solve()
        self.assertEquals(result, 88)

    def test_multiplication(self):
        equation = "8*17"
        solver = get_equation_solver(equation)
        result = solver.solve()
        self.assertEquals(result, 136)

    def test_division(self):
        equation = "12/4"
        solver = get_equation_solver(equation)
        result = solver.solve()
        self.assertEquals(result, 3)
