import os
from pprint import pprint
def append_list(file_name):
    with open(file_name,'rt', encoding='utf-8') as f:
        text_list = f.readlines()
        len_file = len(text_list)
        result_list = [len_file, file_name, len_file, text_list]
        return result_list
text_list = []
text_list.append(append_list('1.txt'))
text_list.append(append_list('2.txt'))
text_list.append(append_list('3.txt'))
text_list.sort()
for file_inf in text_list:
    with open('4.txt', 'a') as file:
        file.writelines(file_inf[1]+'\n')
        file.writelines(str(file_inf[2]) + '\n')
        file.writelines(file_inf[3])
        file.writelines('\n')
pprint(text_list)
