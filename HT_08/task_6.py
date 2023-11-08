# Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора.


def shortest(input_string: str) -> str:
    return f"Мінімальна довжина слова в рядку: {min(len(word) for word in input_string.split())}"


print(shortest("which word from this string is shortest"))
