from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem("Maximize_Beverage_Production", LpMaximize)

lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція
model += lemonade + fruit_juice, "Total_Beverages"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_limit"
model += 1 * lemonade <= 50, "Sugar_limit"
model += 1 * lemonade <= 30, "Lemon_juice_limit"
model += 2 * fruit_juice <= 40, "Fruit_puree_limit"

# Розв’язуємо задачу
model.solve()

# Виводимо результати
print("Lemonade to produce:", int(value(lemonade)))
print("Fruit Juice to produce:", int(value(fruit_juice)))
print("Total products:", int(value(model.objective)))