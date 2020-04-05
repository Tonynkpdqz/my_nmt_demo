import os

new_spa = open('new_spa', "a+", encoding='utf-8')
with open('spa.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_arr = line.split('CC-BY')
        new_spa.write(line_arr[0]+"\n")
        print(line_arr[0])
new_spa.close()