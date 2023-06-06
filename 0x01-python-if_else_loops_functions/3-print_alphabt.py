#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in ['q', 'e']:
        print(chr(letter), end='')
