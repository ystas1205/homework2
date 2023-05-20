with open('1.txt', encoding='utf-8') as file1, \
        open('2.txt', encoding='utf-8') as file2, \
        open('3.txt', encoding='utf-8') as file3, \
        open('file.txt', 'w', encoding='utf-8') as file4:
    dict_file = {'file1': file1.readlines(), 'file2': file2.readlines(), 'file3': file3.readlines()}
    file1.seek(0)
    file2.seek(0)
    file3.seek(0)
    filename_list = ['1.txt', '2txt', '3txt']
    file_lengths = [len(file1.readlines()), len(file2.readlines()), len(file3.readlines())]
    sort_list = file_lengths.sort()
    for dict_file, f_list, f_lengths in zip(sorted(dict_file.values(), reverse=True), filename_list, file_lengths):
        file4.write(f_list + '\n')
        file4.write(str(f_lengths) + '\n')
        file4.write(''.join(dict_file) + '\n')
with open('file.txt', encoding='utf=8') as file4:
    print(file4.read())
