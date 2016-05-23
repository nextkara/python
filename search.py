#!/usr/bin/python
from collections import deque
def search(lines, pattern, history =5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    inputWord = input('please input your word >>>')
    with open('systeminfo.py') as f:
        for line, prevlines in search(f, inputWord, 1):
            for pline in prevlines:
                print(pline, end = '')
            print(line, end = '')
            print('-'*20)
        
