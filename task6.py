

def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    items_ratio = [(item, values['calories'] / values['cost']) for item, values in items.items()]
    # Сортуємо страви за зменшенням співвідношення калорій до вартості
    items_ratio.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    chosen_items = []

    for item, ratio in items_ratio:
        cost = items[item]['cost']
        if budget >= cost:
            budget -= cost
            total_calories += items[item]['calories']
            chosen_items.append(item)

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Ініціалізуємо масив для зберігання максимальних калорій для кожного бюджету
    dp = [0] * (budget + 1)
    item_choice = [None] * (budget + 1)

    for cost in range(1, budget + 1):
        for item, values in items.items():
            item_cost = values['cost']
            item_calories = values['calories']
            if item_cost <= cost:
                if dp[cost - item_cost] + item_calories > dp[cost]:
                    dp[cost] = dp[cost - item_cost] + item_calories
                    item_choice[cost] = item

    total_calories = dp[budget]
    chosen_items = []
    cost = budget

    while cost > 0 and item_choice[cost]:
        chosen_items.append(item_choice[cost])
        cost -= items[item_choice[cost]]['cost']

    return chosen_items, total_calories

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100
    
    print("Жадібний алгоритм:")
    chosen_items, total_calories = greedy_algorithm(items, budget)
    print(f"Вибрані страви: {chosen_items}")
    print(f"Загальна кількість калорій: {total_calories}")

    print("\nДинамічне програмування:")
    chosen_items, total_calories = dynamic_programming(items, budget)
    print(f"Вибрані страви: {chosen_items}")
    print(f"Загальна кількість калорій: {total_calories}")
