file_path = 'files\\demo.txt'
result = [1, 2, 3, 4]

try:
    file1 = open(file_path, 'a')
    file1.write('Something')
    file1.writelines(map(str, result))
except:
    print('File not found')
finally:
    file1.close()