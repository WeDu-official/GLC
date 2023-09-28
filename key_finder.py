import PAPFL,CAPFL,JSAPFL,JAPFL,BAPFL,HAPFL,KTAPFL
def find_between(first_word, second_word, occurrence):
    file = open('main.gcf', 'r')
    lines = file.readlines()
    file.close()
    first_line_number = None
    second_line_number = None
    count = 0

    for i, line in enumerate(lines):
        if first_word in line:
            count += 1
            if count == occurrence:
                first_line_number = i
        if second_word in line and count == occurrence:
            second_line_number = i
            break

    if first_line_number is not None and second_line_number is not None:
        words_between = []
        for i in range(first_line_number + 1, second_line_number):
            line = lines[i].strip()
            words_between.append(lines[i])
        return words_between
    else:
        return []  # If either first_word or second_word is not found in the file or occurrence is not found


def list_to_string(lst):
    string = ''.join(lst)
    string = string.replace('\\n', '\n')
    return string
pycode1 = find_between(f'<python part s>2', f'<python part e>2', 1)
pycode2 = list_to_string(pycode1)
for shortpy,longpy in PAPFL.func_mapping.items():
    if shortpy in pycode2:
        print("------------------------------")
        print("python key got found that is:")
        print(shortpy)
        print("------------------------------")
for shortC,longC in CAPFL.func_mapping.items():
    if shortC in pycode2:
        print("------------------------------")
        print("C key got found that is:")
        print(shortC)
        print("------------------------------")
for shortB,longB in BAPFL.func_mapping.items():
    if shortB in pycode2:
        print("------------------------------")
        print("batch key got found that is:")
        print(shortB)
        print("------------------------------")
for shortKT,longKT in KTAPFL.func_mapping.items():
    if shortKT in pycode2:
        print("------------------------------")
        print("kotlin key got found that is:")
        print(shortKT)
        print("------------------------------")
for shortJ,longJ in JAPFL.func_mapping.items():
    if shortJ in pycode2:
        print("------------------------------")
        print("java key got found that is:")
        print(shortJ)
        print("------------------------------")
for shortJs,longJs in JSAPFL.func_mapping.items():
    if shortJs in pycode2:
        print("------------------------------")
        print("javascript key got found that is:")
        print(shortJs)
        print("------------------------------")
for shorth,longh in HAPFL.func_mapping.items():
    if shorth in pycode2:
        print("------------------------------")
        print("html key got found that is:")
        print(shorth)
        print("------------------------------")