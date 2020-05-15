import random, time, os

chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '+', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', ':', ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ",", ".", "/", "{", "}", '"', ":", ">", "?", "'"]
os.system('clear')
heigth, width = os.popen('stty size', 'r').read().split()
heigth = int(heigth)
width = int(width)

colors = {
    'default': '\033[01;34m',
    'end': '\033[37m',
    'console': '\033[37m',
}

def new_matrix(width):
    matrix_lines = []
    add_line = []
    for _ in range(width):
        if random.randint(0, 5):
            add_line.append(' ')
        else:
            add_line.append(chars[random.randint(0, len(chars)-1)])
    matrix_lines.append(add_line)
    return matrix_lines

matrix_lines = new_matrix(width)
print(colors['default'])
try:
    while True:
        heigth_n, width_n = os.popen('stty size', 'r').read().split()
        heigth_n = int(heigth_n)
        width_n = int(width_n)
        if width_n != width or heigth_n != heigth:
            matrix_lines = new_matrix(width_n)
            width = width_n
            heigth = heigth_n
        os.system('clear')
        add_line = []
        for char in matrix_lines[0]:
            if char != " " and random.randint(0, 30):
                add_line.append(chars[random.randint(0, len(chars)-1)])
            elif not random.randint(0, 300) and char == ' ':
                add_line.append(colors['end'] + chars[random.randint(0, len(chars)-1)] + colors['default'])
            else:
                add_line.append(' ')
        matrix_lines.insert(0, add_line)
        if len(matrix_lines)+1 > heigth:
            matrix_lines.pop(len(matrix_lines)-1)
        for line in matrix_lines:
            for char in line:
                print(char, end='')
            print('')
        time.sleep(0.01)
except KeyboardInterrupt:
    print(colors['console'])
    os.system('clear')