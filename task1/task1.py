# Чтение списка чисел от пользователя
input_str = input("Введите числа через запятую: ")
numbers = [int(num.strip()) for num in input_str.split(',')]

# Вывод четных чисел
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Четные числа: {even_numbers}")

# Нахождение максимального и минимального числа
max_num = max(numbers)
min_num = min(numbers)
print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")

# Сортировка списка в порядке возрастания без использования встроенной функции sorted() 
# Сортировка пузырьком
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_list = bubble_sort(numbers)
print(f"Отсортированный список: {sorted_list}")
