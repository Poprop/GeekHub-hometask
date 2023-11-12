x = f"Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл також додайте в " \
    f"репозиторій. На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу." \
    f"Кількість символів в блоках - та, яка введена в другому параметрі. Придумайте самі, як обробляти помилку, наприклад," \
    f"коли кількість символів більша, ніж є в файлі або, наприклад, файл із двох символів і треба вивести по одному символу," \
    f"то що виводити на місці середнього блоку символів?). Не забудьте додати перевірку чи файл існує."

with open("example.txt", "w", encoding="utf-8") as f:
    for el in x.split():
        f.write(el + "\n")


def process_file(file_name, block_size):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read().replace('\n', '')
            total_chars = len(content)

            if block_size > total_chars:
                raise ValueError("Кількість символів перевищує загальну кількість символів у файлі.")

            middle = total_chars // 2
            half_block_size = block_size // 2

            start_block = content[:block_size]
            middle_block = content[middle - half_block_size: middle + half_block_size]
            end_block = content[-block_size:]

            return [start_block, middle_block, end_block]

    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


file_name = "example.txt"
block_size = 5
blocks = process_file(file_name, block_size)
print(blocks)
