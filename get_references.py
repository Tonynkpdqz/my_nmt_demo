import os


def get_references_and_candidate(filename,rows_length):
    list_all = [[]]
    with open(filename, 'r', encoding='utf-8') as f:
        for i in range(1,rows_length):
            line = f.readline().rstrip()
            line_arr = line.split('	')
            in_list = []
            in_list.append(line_arr[0])
            in_list.append(line_arr[1])
            list_all.append(in_list)
        return list_all
        '''lines = f.readlines()
        for line in lines:
            line_arr = line.split('	')
            print(line_arr[0])'''
