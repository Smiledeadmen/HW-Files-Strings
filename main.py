import os

all_data = {}
sort_dict = {}
FILE_LIBS_DIR = 'libs'
FILE_RESULT = 'result.txt'
BASE_PATH = os.getcwd()
libs_file_path = os.path.join(BASE_PATH, FILE_LIBS_DIR)
result_file_path = os.path.join(BASE_PATH, FILE_RESULT)
print(f'----> {libs_file_path}')


def file_worker(file_path, mode, data):
  with open(file_path, mode, encoding='utf8') as file:
      for key, values in data.items():
        file.write(f'{key}\n')
        for val in values:
            file.write(f'{val}\n')


def sorted_dict(dict):
    sorted_keys = sorted(dict, key=dict.get)
    for key in sorted_keys:
        sort_dict[key] = dict[key]
    return sort_dict


def get_data_from_files():
    list = [x for x in os.listdir(libs_file_path) if x.endswith('.txt')]
    print(list)
    for file_name in list:
        with open(os.path.join(libs_file_path, file_name), 'r', encoding='utf8') as file:
            count_lines = sum(1 for lines in file)
            file.seek(0)
            data = file.read()
            all_data[file_name] = [count_lines, data]
    print(all_data)


# получение списка фалов из каталога libs, открытие каждого фалйла по очереди для подсчета строк и содеджимого в словарь all_data
get_data_from_files()

# сортировка словваря по значению, возвращается отсортированный словарь
sorted_dict(all_data)

# Запись значений в файл result.txt в корневом каталоге.
file_worker(result_file_path, 'a', sort_dict)
