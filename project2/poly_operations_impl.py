import numpy as np
import matplotlib.pyplot as plt
from itertools import zip_longest

class Polynomial:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)

    def __repr__(self):
        return "Polynomial" + str(self.coefficients)

    def __call__(self, x):
        res = 0
        for i, coeff in enumerate(self.coefficients):
            res += coeff * (x ** (len(self.coefficients) - 1 - i))
        return res

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_len - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_len - len(other.coefficients))
        result_coeffs = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(*result_coeffs)

    def __sub__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_len - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_len - len(other.coefficients))
        result_coeffs = [a - b for a, b in zip(padded_self, padded_other)]
        return Polynomial(*result_coeffs)

    def __mul__(self, other):
        result_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result_coeffs[i + j] += a * b
        return Polynomial(*result_coeffs)

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            degree = len(self.coefficients) - 1 - i
            if coeff != 0:
                sign = '+' if coeff > 0 and i != 0 else ''
                term = f"{sign}{coeff}" if abs(coeff) != 1 or degree == 0 else sign
                term += 'x' if degree != 0 else ''
                term += f"^{degree}" if degree > 1 else ''
                terms.append(term)
        return ' '.join(terms)

# Definir los polinomios de entrada
p1 = Polynomial(-3, 0, 0,2, -7)
p2 = Polynomial(5, -8, 0, 0, 10)

# Realizar las operaciones
sum_result = p1 + p2
sub_result = p1 - p2
mul_result = p1 * p2

# Imprimir los resultados
print("p1(x) =", p1)
print("p2(x) =", p2)
print("p1(x) + p2(x) =", sum_result)
print("p1(x) - p2(x) =", sub_result)
print("p1(x) * p2(x) =", mul_result)

# Graficar los polinomios y sus operaciones en el intervalo [-20, 20]
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 400)
y_p1 = p1(x)
y_p2 = p2(x)
y_sum = sum_result(x)
y_sub = sub_result(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y_p1, label='p1(x)', linewidth=2)
plt.plot(x, y_p2, label='p2(x)', linewidth=2)
plt.plot(x, y_sum, label='p1(x) + p2(x)', linestyle='dashed', linewidth=2)
plt.plot(x, y_sub, label='p1(x) - p2(x)', linestyle='dashed', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomios y sus Operaciones')
plt.legend()
plt.grid(True)
plt.show()
# Graficar el producto de los polinomios en una gráfica diferente
y_mul = mul_result(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y_mul, label='p1(x) * p2(x)', color='green', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Producto de p1(x) y p2(x)')
plt.legend()
plt.grid(True)
plt.show()