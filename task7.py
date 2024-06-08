

import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків двох кубиків
def simulate_dice_rolls(num_rolls):
    results = [0] * 13  # Масив для підрахунку випадків сум від 2 до 12
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1
    return results

# Функція для обчислення ймовірностей
def calculate_probabilities(results, num_rolls):
    probabilities = [0] * 13
    for i in range(2, 13):
        probabilities[i] = (results[i] / num_rolls) * 100
    return probabilities

# Функція для порівняння результатів з аналітичними розрахунками
def compare_with_analytical(probabilities):
    analytical_probabilities = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }

    print("Сума\tІмовірність (симуляція)\tІмовірність (аналітична)")
    for i in range(2, 13):
        print(f"{i}\t{probabilities[i]:.2f}%\t\t\t{analytical_probabilities[i]}%")

# Симуляція
num_rolls = 1000000
results = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(results, num_rolls)

# Порівняння результатів з аналітичними розрахунками
compare_with_analytical(probabilities)

# Візуалізація результатів
sums = list(range(2, 13))
analytical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

plt.bar(sums, probabilities[2:], color='blue', alpha=0.7, label='Симуляція')
plt.plot(sums, analytical_probabilities, color='red', marker='o', label='Аналітичні')

plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Імовірність (%)')
plt.title('Імовірність сум при киданні двох кубиків')
plt.legend()
plt.show()
