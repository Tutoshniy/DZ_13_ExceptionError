import os
from exception_new import FileException

'Задание 1 из Домашнего задания 7'


def group_rename_files(new_name: str = None, num_digits: int = None, source_ext: str = None, file_ext: str = None,
                       name_range=None):
    counter = 1
    if new_name is None:
        raise FileException('new_name')
    elif num_digits is None:
        raise FileException('num_digits')
    elif source_ext is None:
        raise FileException('source_ext')
    elif file_ext is None:
        raise FileException('file_ext')
    for filename in os.listdir('.'):
        if filename.endswith(source_ext):
            if name_range:
                original_name = filename[name_range[0] - 1:name_range[1]]
                new_filename = f'{original_name}{new_name}_{str(counter).zfill(num_digits)}{file_ext}'
            else:
                new_filename = f'{new_name}_{str(counter).zfill(num_digits)}{file_ext}'
            os.rename(filename, new_filename)
            counter += 1


if __name__ == "__main__":
    group_rename_files("прикол", 3, '.txt')
