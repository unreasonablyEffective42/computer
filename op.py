
with open('opcodes.txt', 'w') as ops:
    sources= ['A','B','C','RAM']
    registers = ['A','B','C']
    n = 1
    m = 1

    print("MEMORY OPS",file = ops)
    for s in sources:
        for d in sources:
            if d != s:
                print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'), (s + "->" + d),file = ops)
                n = n+1

    print("\nALU OPS NO STORE",file = ops)
    for a in registers:
        for b in registers:
            if a != b:
                print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"IN1:", a, "op IN2:", b,file = ops)
                n = n+1

    print("\nALU MEMORY OPS",file = ops)
    for a in registers:
        for b in registers:
            if a != b:
                for d in sources:
                    print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"IN1:", a, "op IN2:", b, "->", d,file = ops)
                    n = n+1

    print("\nPROGRAM COUNTER",file = ops)
    print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"D-LINE->PC",file = ops)
    n=n+1
    print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"RAM->PC",file = ops)
    n=n+1
    print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"PC->A-LINE",file = ops)
    n=n+1
    print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"PC->D-LINE",file = ops)
    n=n+1
    for a in registers:
        print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"IN1: PC op IN2:", a,file = ops)
        n=n+1
    for a in registers:
        print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"IN1:", a,"op IN2: PC",file = ops)
        n=n+1

    print("\nSINGLE IO OPS",file = ops)
    for a in registers:
        print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"IN1:", a,file = ops)
        n=n+1
    for a in registers:
        for b in sources:
                print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"IN1:", a,"OP->",b,file = ops)
                n=n+1
    for a in sources:
        print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'), a,"->D-LINE",file = ops)
        n=n+1
    for a in registers:
        print(format(n,'#03d'),format(n,'#04X'),format(n,'#010b'),"D-LINE->",a,file = ops)
        n = n + 1

    print("\nALU OPS",file = ops)
    operations = ['ADD','SUB','INC','DEC','AND','NAD','ORR','NOR','XOR','XNR','CMP']
    for op in operations:
        print(format(m,'#03d'),format(m,'#04X'),format(m,'#010b'),op,file = ops)
        m=m+1

    print("\nJUMPS",file = ops)
    print("\nNULLNARY JUMPS", file = ops)
    njumps = ['JMP','JCF','JNC','JZF','JNZ']
    for jump in njumps:
        print(format(m,'#03d'),format(m,'#04X'),format(m,'#010b'),jump,file = ops)
        m = m + 1
    print("\nUNARY JUMPS",file = ops)
    ujumps = ['JEZ','JGZ']
    regs =  ['A','B','C','PC']
    for jump in ujumps:
        for reg in regs:
            print(format(m,'#03d'),format(m,'#04X'),format(m,'#010b'),jump,reg,file = ops)
            m = m + 1

    print("\nBINARY JUMPS",file = ops)
    bjumps = ['JGT','JLT']
    for jump in bjumps:
        for rega in regs:
            for regb in regs:
                if rega != regb:
                    print(format(m,'#03d'),format(m,'#04X'),format(m,'#010b'),jump,rega,regb,file = ops)
                    m = m + 1


    for rega in regs:
        for regb in regs:
            if rega < regb:
                print(format(m,'#03d'),format(m,'#04X'),format(m,'#010b'),'JEQ',rega,regb,file = ops)
                m = m + 1

    print("\nBITSHIFTS", file = ops)
    for op in ['SHL','SHR']:
        for reg in registers:
            print(format(m,'#03d'),format(m,'#04X'),format(m,'#010b'),op,reg,file = ops)
            m = m + 1

    print("\nTERMINATION AND EXIT CODES", file = ops)
    m=255
    print(format(m,'#03d'),format(m,'#04X'),format(m,'#010b'),"HALT",file = ops)
