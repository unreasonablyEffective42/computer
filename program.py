with open('program1.asm', 'w') as ops:
    for n in range (255):
        print(format(n,'#03d'),format(n,'#04X'), file = ops)