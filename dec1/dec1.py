import re

list1 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

def digitize(x):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    done = False
    j=0
    while not done:
        w = re.search('|'.join(digits), x)
        if w is None:
            done = True
            break
        x = x[:w.start()] + str(digits.index(w.group())+1) + x[w.start()+1:]
    return x

# with open('input.txt', 'r') as f:
#     f = list1
#     print([(line, digitize(line)) for line in f])
with open('input.txt', 'r') as f:    
    print(
        sum(
            [int(''.join(
                    [''.join(
                        re.findall(
                            '\d+'
                            , ''.join(digitize(line))
                        )
                    )[i] for i in [0,-1]]
                )
            ) for line in f]
        )
    )