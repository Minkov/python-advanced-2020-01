from os import listdir, walk
from os.path import join, isdir, isfile


def traverse_directory_tree(folder_path, on_file_found):
    paths = [join(folder_path, content) for content in listdir(folder_path)]
    [on_file_found(file) for file in paths if isfile(file)]
    [traverse_directory_tree(dir, on_file_found) for dir in paths if isdir(dir)]


def does_file_contain_text(file_path, text):
    with open(file_path, 'r') as file:
        line = file.readline()
        while line:
            if text in line:
                return True
            line = file.readline()
        return False


def print_file_if_containing_text(text):
    def print_file_if_containing_text_internal(file_path):
        if does_file_contain_text(file_path, text):
            print(file_path)

    return print_file_if_containing_text_internal


folder_path = 'files'
traverse_directory_tree(folder_path, print_file_if_containing_text('met'))
traverse_directory_tree(folder_path, print_file_if_containing_text('sum'))

print(list(walk('files')))
