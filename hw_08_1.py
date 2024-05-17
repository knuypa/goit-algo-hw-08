import heapq

def min_cost_to_connect_cables(cables):
    # Створити мінімальну купу з початкових довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного кабеля
    while len(cables) > 1:
        # Вийняти два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на їх об'єднання
        cost = first + second
        total_cost += cost
        
        # Помістити новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))