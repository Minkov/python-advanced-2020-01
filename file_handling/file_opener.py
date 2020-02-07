file_path = 'files\\text3.txt'

try:
    open(file_path)
    print('File found')
except FileNotFoundError as e:
    print(e)
    print('File not found')
except:
    print('Unknown exception')
finally:
    print('End')