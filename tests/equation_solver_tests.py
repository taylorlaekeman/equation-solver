from unittest import TestCase

from equation_solver.equation_solver import solve


class EquationSolverTests(TestCase):
    def test_addition(self):
        equation = "9+1"
        result = solve(equation)
        self.assertEquals(result, 10)

    def test_subtraction(self):
        equation = "92-4"
        result = solve(equation)
        self.assertEquals(result, 88)

    def test_multiplication(self):
        equation = "8*17"
        result = solve(equation)
        self.assertEquals(result, 136)

    def test_division(self):
        equation = "12/4"
        result = solve(equation)
        self.assertEquals(result, 3)
