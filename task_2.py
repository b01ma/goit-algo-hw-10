import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


# Кількість випадкових точок
N = 100000

# Межі інтегрування
a = 0
b = 2

# Функція
def f(x):
    return x ** 2

# Генерація випадкових x у межах [a, b]
x_random = np.random.uniform(a, b, N)

# Обчислення середнього значення функції на випадкових x
mean_value = np.mean(f(x_random))

# Обчислення інтеграла
monte_carlo_result = (b - a) * mean_value

# Аналітичне обчислення за допомогою scipy
quad_result, _ = quad(f, a, b)

print(f"Метод Монте-Карло: {monte_carlo_result:.5f}")
print(f"Аналітичний (quad): {quad_result:.5f}")
print(f"Похибка: {abs(monte_carlo_result - quad_result):.5f}")
