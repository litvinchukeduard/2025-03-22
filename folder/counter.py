from collections import defaultdict, Counter
'''
У файлі записані випадкові числа 5, 0, 5, 3, 7, 3, 8, 7, 1, 4, 1, 0, 3, 5, 3, 5, 6, 0, 7, 9, 0, 8, 9, 4, 2, 3, 3, 2, 7, 1
Потрібно написати функцію, яка буде рахувати кількість появи кожного числа, 
та виведе найчастіше число у термінал
'''

# 1. Просчитати рядки з файлу
def read_lines_from_file(file_path: str) -> list[str]:
    with open(file_path, encoding='utf-8') as file:
        return file.readlines()

# print(__file__) 
# print(read_lines_from_file('/Users/eddielitvinchuk/Documents/Repositories/2025-03-22/folder/counter.txt'))

# print(read_lines_from_file('./folder/counter.txt'))
'5, 0, 5, 3, 7, 3\n'

# 2. З цього рядка дістати окремі числа

# r''
# my_str = '5, 0, 5, 3, 7, 3\n'.strip()
# print(my_str.split(', '))

def convert_file_line_to_numbers_list(line: str) -> list[int]:
    numbers_list = []
    numbers_str_list = line.strip().split(', ')
    for number_str in numbers_str_list:
        numbers_list.append(int(number_str))
    return numbers_list

# print(convert_file_line_to_numbers_list('5, 0, 5, 3, 7, 3\n'))
# [5, 0, 5, 3, 7, 3]

# 5 -> 2, 0 -> 1, 3 -> 2, 7 -> 1
# {5: 2, 0: 1, 3: 2, 7: 1}

# 3. Потрібно пройтися по числам та порахувати повторення кожного

def calculate_statistics(element_list: list[int]) -> dict[int, int]:
    statistics_dict = {}
    for element in element_list:
        # Зустрічаємо елемент перший раз
        if element not in statistics_dict:
            statistics_dict[element] = 0
            # Створити новий ключ та задати значення як 1
        statistics_dict[element] += 1
        # Зустрічаємо елемент невперше
            # Прочитати попереднє значення та збільшити його на 1
    return statistics_dict

def calculate_statistics_default_dict(element_list: list[int]) -> dict[int, int]:
    statistics_dict = defaultdict(int)
    for element in element_list:
        statistics_dict[element] += 1
    return statistics_dict

def calculate_statistics_counter(element_list: list[int]) -> Counter:
    return Counter(element_list)

# print(Counter([1, 2, 3, 3, 4]))

def main():
    file_path = './folder/counter.txt'
    lines = read_lines_from_file(file_path)

    numbers_list = []
    for line in lines:
        numbers_list.extend(convert_file_line_to_numbers_list(line))

    print(numbers_list)

    print(calculate_statistics_counter(numbers_list))
    # calculate_statistics_default_dict(
    #     convert_file_line_to_numbers_list( 
    #         convert_file_line_to_numbers_list(file_path)
    #     )
    # )

main()
    
        

# print(calculate_statistics_default_dict([5, 0, 5, 3, 7, 3]))

# my_list = [1, 2, 3, 4]
# my_dict = {'a': 1, 'b': 2}
# my_dict += 1
# print('b' in my_dict)

# my_dict = {}
# my_dict[10] += 1

# my_default_dict = defaultdict(tuple)
# print(my_default_dict)
# my_default_dict[10].count('a')
# print(my_default_dict)
