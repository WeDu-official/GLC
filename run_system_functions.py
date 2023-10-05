import JAPFL
import JSAPFL
import PAPFL
import HAPFL
import CAPFL
import KTAPFL
import BAPFL
import DAPFL
import AFM
import time
import os
import subprocess
start_time = time.time()
command2 = ''
command = "python runned_code.py"
token_message = ''
token_message2 = ''
token_message3 = ''
token_message4 = ''
programminglanguagefileformat = '.py'
func_mapping_var = {}
func_mapping_var2 = {}
with open('options.txt', 'r') as options_Reader:
    options = options_Reader.read()
def normal_function_mapping(code:str,function_mapping_variable:dict):
    # sourcery skip: missing-dict-items
    lines2 = code.strip().split("\n")
    for s in range(len(lines2)):
        for short, full in function_mapping_variable:
            lines2[s] = lines2[s].replace(short, full)
    return "\n".join(lines2)
def find_between(filepath,first_word, second_word, occurrence):
    with open(filepath, 'r') as file:
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

def find_between2(code:str,first_word, second_word, occurrence):
    lines = code.strip().split("\n")
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
def find_between2_2(code:str,first_word, second_word, occurrence):
    lines = code.split("\n")
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

def find_between3(text, firstword, secondword):
    start_index = text.find(firstword) + len(firstword)
    end_index = text.find(secondword)
    if start_index == -1 or end_index == -1:
        return None
    return text[start_index:end_index]

def list_to_string(lst):
    string = ''.join(lst)
    return string.replace('\\n', '\n')
def list_to_string2(lst):
    string = '\n'.join(lst)
    return string.replace('\\n', '\n')
def compile(mode:str,file_path:str,thecode:str,programminglanguage:str):
    command2 = ''
    options_Reader = open('options.txt', 'r')
    if thecode == '' and file_path != '':
        co = open(file_path,'r')
        code = co.read()
        co.close()
    if thecode != '' and file_path == '':
        code = thecode
    else:
        print('no data')
        code = ''
    options = options_Reader.read()
    SET_NO_STATEMENT_FUNCTION_CALLING = list_to_string(find_between2(options, '$<set no statement function calling>','/set no statement function calling>$', 1))
    options_Reader.close()
    prt = ''
    prt2 = ''
    prt3 = ''
    prt4 = ''
    prt5 = ''
    prt6 = ''
    prt7 = ''
    prt8 = ''
    start_time = time.time()
    x = int(time.strftime('%Y%d%d%H%M%S'))
    command = "python runned_code.py"
    token_message = ''
    token_message2 = ''
    token_message3 = ''
    token_message4 = ''
    programminglanguagefileformat = '.py'
    func_mapping_var = {}
    func_mapping_var2 = {}
    if programminglanguage == 'python':
        func_mapping_var = PAPFL.func_mapping.items()
        func_mapping_var2 = PAPFL.func_mapping.keys()
    if programminglanguage == 'C' or programminglanguage == 'c':
        func_mapping_var = CAPFL.func_mapping.items()
        func_mapping_var2 = CAPFL.func_mapping.keys()
    if programminglanguage == 'java':
        func_mapping_var = JAPFL.func_mapping.items()
        func_mapping_var2 = JAPFL.func_mapping.keys()
    if programminglanguage == 'javascript' or programminglanguage == 'JS':
        func_mapping_var = JSAPFL.func_mapping.items()
        func_mapping_var2 = JSAPFL.func_mapping.keys()
    if programminglanguage == 'batch':
        func_mapping_var = BAPFL.func_mapping.items()
        func_mapping_var2 = BAPFL.func_mapping.keys()
    if programminglanguage == 'kotlin':
        func_mapping_var = KTAPFL.func_mapping.items()
        func_mapping_var2 = KTAPFL.func_mapping.keys()
    if programminglanguage == 'html':
        func_mapping_var = HAPFL.func_mapping.items()
        func_mapping_var2 = HAPFL.func_mapping.keys()
    if programminglanguage == 'data':
        func_mapping_var = DAPFL.func_mapping.items()
        func_mapping_var2 = DAPFL.func_mapping.keys()
    else:
        func_mapping_var = PAPFL.func_mapping.items()
        func_mapping_var2 = PAPFL.func_mapping.keys()
    if programminglanguage != 'python' and programminglanguage != 'C' and programminglanguage != 'c' and programminglanguage != 'java' and programminglanguage != 'javascript' and programminglanguage != 'JS' and programminglanguage != 'batch' and programminglanguage != 'kotlin' and programminglanguage != 'html' and programminglanguage != 'data':
        print("unknown programming language")
        exit()
    lines = code.strip().split("\n")
    a = list(func_mapping_var)
    b = list(func_mapping_var2)
    for i in range(len(lines)):
        if mode == 'f':
            data1 = find_between(file_path, b[-7], b[-6], i + 1)
            data = list_to_string(data1)
            data2 = find_between(file_path, b[-5], b[-4], i + 1)
            data_2 = list_to_string(data2)
            data_3 = find_between(file_path, b[-7], b[-9], i + 1)
            data3 = list_to_string(data_3)
            data_4 = find_between(file_path, b[-5], b[-8], i + 1)
            data4 = list_to_string(data_4)
        if mode == 'c':
            data1 = find_between2(code, b[-7], b[-6], i + 1)
            data = list_to_string(data1)
            data2 = find_between2(code, b[-5], b[-4], i + 1)
            data_2 = list_to_string(data2)
            data_3 = find_between2(code, b[-7], b[-9], i + 1)
            data3 = list_to_string(data_3)
            data_4 = find_between2(code, b[-5], b[-8], i + 1)
            data4 = list_to_string(data_4)
        data1 = find_between2("\n".join(lines), b[-7], b[-6], i + 1)
        data = list_to_string(data1)
        data2 = find_between2("\n".join(lines), b[-5], b[-4], i + 1)
        data_2 = list_to_string(data2)
        data3 = find_between2("\n".join(lines), b[-7], b[-9], i + 1)
        data_3 = list_to_string(data3)
        data4 = find_between2("\n".join(lines), b[-5], b[-8], i + 1)
        data_4 = list_to_string(data4)
        semi_fin_lines = code.strip().split("\n")
        code_texted = "\n".join(semi_fin_lines)
        goto = find_between3(code_texted, b[-7], b[-6])
        goto2 = find_between3(code_texted, b[-5], b[-4])
        goto3 = find_between3(code_texted, b[-7], b[-9])
        goto4 = find_between3(code_texted, b[-5], b[-8])
        if goto == '' or goto == '\n' or goto == '\t' or goto == None:
            goto = ''
        if goto2 == '' or goto2 == '\n' or goto2 == '\t' or goto2 == None:
            goto2 = ''
        if goto3 == '' or goto3 == '\n' or goto3 == '\t' or goto3 == None:
            goto3 = ''
        if goto4 == '' or goto4 == '\n' or goto4 == '\t' or goto4 == None:
            goto4 = ''
        tokens_shape = f'''$<
{data}
/tokened>$'''
        em_tokens_shape = f'''$<
/tokened>$'''
        tokens_shape2 = f'''%<
{data_2}
/tokened>%'''
        em_tokens_shape2 = f'''%<
/tokened>%'''
        function_shape = f'''$<
{data_3}
/function>$'''
        em_function_shape = f'''$<
/function>$'''
        function_shape2 = f'''%<
{data_4}
/function>%'''
        em_function_shape2 = f'''%<
/function>%'''
        if programminglanguage == 'data':
            prt = AFM.parser.parse(data)
            prt2 = AFM.parser.parse(goto)
            prt3 = AFM.parser.parse(data_2)
            prt4 = AFM.parser.parse(goto2)
            prt5 = normal_function_mapping(data_3, func_mapping_var)# type: ignore
            prt6 = normal_function_mapping(goto3, func_mapping_var)# type: ignore
            prt7 = normal_function_mapping(data_4, func_mapping_var)# type: ignore
            prt8 = normal_function_mapping(goto4, func_mapping_var)# type: ignore
        if programminglanguage == 'python':
            prt = f'print("{AFM.parser.parse(data)}")'
            prt2 = f'print("{AFM.parser.parse(goto)}")'
            prt3 = f'{AFM.parser.parse(data_2)}'
            prt4 = f'{AFM.parser.parse(goto2)}'
            prt5 = f'print("{normal_function_mapping(data_3, func_mapping_var)}")'# type: ignore
            prt6 = f'print("{normal_function_mapping(goto3, func_mapping_var)}")'# type: ignore
            prt7 = f'{normal_function_mapping(data_4, func_mapping_var)}'# type: ignore
            prt8 = f'{normal_function_mapping(goto4, func_mapping_var)}'# type: ignore
            token_message = '#empty tokened function $'
            token_message2 = '#empty tokened function %'
            token_message3 = '#empty function $'
            token_message4 = '#empty function %'
        if programminglanguage == 'C' or programminglanguage == 'c':
            prt = f'printf("{AFM.parser.parse(data)}");'
            prt2 = f'printf("{AFM.parser.parse(goto)}");'
            prt3 = f'{AFM.parser.parse(data_2)}'
            prt4 = f'{AFM.parser.parse(goto2)}'
            prt5 = f'printf("{normal_function_mapping(data_3, func_mapping_var)}");'# type: ignore
            prt6 = f'printf("{normal_function_mapping(goto3, func_mapping_var)}");'# type: ignore
            prt7 = f'{normal_function_mapping(data_4, func_mapping_var)}'# type: ignore
            prt8 = f'{normal_function_mapping(goto4, func_mapping_var)}'# type: ignore
            token_message = '//empty tokened function $'
            token_message2 = '//empty tokened function %'
            token_message3 = '//#empty function $'
            token_message4 = '//#empty function %'
        if programminglanguage == 'java':
            prt = f'System.out.println("{AFM.parser.parse(data)}");'
            prt2 = f'System.out.println("{AFM.parser.parse(goto)}");'
            prt3 = f'{AFM.parser.parse(data_2)}'
            prt4 = f'{AFM.parser.parse(goto2)}'
            prt5 = f'System.out.println("{normal_function_mapping(data_3, func_mapping_var)}");'# type: ignore
            prt6 = f'System.out.println("{normal_function_mapping(goto3, func_mapping_var)}");'# type: ignore
            prt7 = f'{normal_function_mapping(data_4, func_mapping_var)}' # type: ignore
            prt8 = f'{normal_function_mapping(goto4, func_mapping_var)}'# type: ignore
            token_message = '//empty tokened function $'
            token_message2 = '//empty tokened function %'
            token_message3 = '//#empty function $'
            token_message4 = '//#empty function %'
        if programminglanguage == 'javascript' or programminglanguage == 'JS':
            prt = f'console.log("{AFM.parser.parse(data)}")'
            prt2 = f'console.log("{AFM.parser.parse(goto)}")'
            prt3 = f'{AFM.parser.parse(data_2)}'
            prt4 = f'{AFM.parser.parse(goto2)}'
            prt5 = f'console.log("{normal_function_mapping(data_3, func_mapping_var)}")'# type: ignore
            prt6 = f'console.log("{normal_function_mapping(goto3, func_mapping_var)}")'# type: ignore
            prt7 = f'{normal_function_mapping(data_4, func_mapping_var)}'# type: ignore
            prt8 = f'{normal_function_mapping(goto4, func_mapping_var)}'# type: ignore
            token_message = '//empty tokened function $'
            token_message2 = '//empty tokened function %'
            token_message3 = '//empty function $'
            token_message4 = '//empty function %'
        if programminglanguage == 'batch':
            prt = f'echo {AFM.parser.parse(data)}'
            prt2 = f'echo {AFM.parser.parse(goto)}'
            prt3 = f'{AFM.parser.parse(data_2)}'
            prt4 = f'{AFM.parser.parse(goto2)}'
            prt5 = f'echo {normal_function_mapping(data_3, func_mapping_var)}'# type: ignore
            prt6 = f'echo {normal_function_mapping(goto3, func_mapping_var)}'# type: ignore
            prt7 = f'{normal_function_mapping(data_4, func_mapping_var)}'# type: ignore
            prt8 = f'{normal_function_mapping(goto4, func_mapping_var)}'# type: ignore
            token_message = 'echo empty tokened function $'
            token_message2 = 'echo empty tokened function %'
            token_message3 = 'echo empty function $'
            token_message4 = 'echo empty function %'
        if programminglanguage == 'kotlin':
            prt = f'println("{AFM.parser.parse(data)}")'
            prt2 = f'println("{AFM.parser.parse(goto)}")'
            prt3 = f'{AFM.parser.parse(data_2)}'
            prt4 = f'{AFM.parser.parse(goto2)}'
            prt5 = f'println("{normal_function_mapping(data_3, func_mapping_var)}")'# type: ignore
            prt6 = f'println("{normal_function_mapping(goto3, func_mapping_var)}")'# type: ignore
            prt7 = f'{normal_function_mapping(data_4, func_mapping_var)}'# type: ignore
            prt8 = f'{normal_function_mapping(goto4, func_mapping_var)}'# type: ignore
            token_message = '//empty tokened function $'
            token_message2 = '//empty tokened function %'
            token_message3 = '//empty function $'
            token_message4 = '//empty function %'
        if programminglanguage == 'html':
            prt = f'<p>{AFM.parser.parse(data)}</p>'
            prt2 = f'<p>{AFM.parser.parse(goto)}</p>'
            prt3 = f'{AFM.parser.parse(data_2)}'
            prt4 = f'{AFM.parser.parse(goto2)}'
            prt5 = f'<p>{normal_function_mapping(data_3, func_mapping_var)}</p>'# type: ignore
            prt6 = f'<p>{normal_function_mapping(goto3, func_mapping_var)}</p>'# type: ignore
            prt7 = f'{normal_function_mapping(data_4, func_mapping_var)}'# type: ignore
            prt8 = f'{normal_function_mapping(goto4, func_mapping_var)}'# type: ignore
            token_message = '//empty tokened function $'
            token_message2 = '//empty tokened function %'
            token_message3 = '//empty function $'
            token_message4 = '//empty function %'
        if programminglanguage != 'python' and programminglanguage != 'C' and programminglanguage != 'c' and programminglanguage != 'java' and programminglanguage != 'javascript' and programminglanguage != 'JS' and programminglanguage != 'batch' and programminglanguage != 'kotlin' and programminglanguage != 'html' and programminglanguage != 'data':
            print("unknown programming language")
            exit()
        if data != '' and data != '\n' and data != '\t':
            codes = code_texted.replace(tokens_shape, prt)
        if f'{b[-7]}{goto}{b[-6]}' in code_texted:
            codes = code_texted.replace(f'{b[-7]}{goto}{b[-6]}', prt2)
        else:
            codes = code_texted.replace(em_tokens_shape, token_message)
        semi_fin_lines2 = codes.strip().split("\n")
        code_texted2 = "\n".join(semi_fin_lines2)
        if data_2 != '' and data_2 != '\n' and data_2 != '\t':
            codes2 = code_texted2.replace(tokens_shape2, prt3)
        if f'{b[-5]}{goto2}{b[-4]}' in code_texted2:
            codes2 = code_texted2.replace(f'{b[-5]}{goto2}{b[-4]}', prt4)
        else:
            codes2 = code_texted2.replace(em_tokens_shape2, token_message2)
        fin_lines = codes2.strip().split("\n")
        code_texted3 = "\n".join(fin_lines)
        if data_3 != '' and data_3 != '\n' and data_3 != '\t':
            if SET_NO_STATEMENT_FUNCTION_CALLING == 'False':
                codes3 = code_texted3.replace(function_shape, prt5)
            else:
                lines = code_texted3.strip().split("\n")
                for i in range(len(lines)):
                    for short, full in func_mapping_var:
                        lines[i] = lines[i].replace(short, full)
                codes3 = "\n".join(lines)
        if f'{b[-7]}{goto3}{b[-9]}' in code_texted3:
            if SET_NO_STATEMENT_FUNCTION_CALLING == 'False':
                codes3 = code_texted3.replace(f'{b[-7]}{goto3}{b[-9]}', prt6)
            else:
                lines = code_texted3.strip().split("\n")
                for i in range(len(lines)):
                    for short, full in func_mapping_var:
                        lines[i] = lines[i].replace(short, full)
                codes3 = "\n".join(lines)
        else:
            if SET_NO_STATEMENT_FUNCTION_CALLING == 'False':
                codes3 = code_texted3.replace(em_function_shape, token_message3)
            else:
                lines = code_texted3.strip().split("\n")
                for i in range(len(lines)):
                    for short, full in func_mapping_var:
                        lines[i] = lines[i].replace(short, full)
                codes3 = "\n".join(lines)
        fin_lines2 = codes3.strip().split("\n")
        code_texted4 = "\n".join(fin_lines2)
        if data_4 != '' and data_4 != '\n' and data_4 != '\t':
            if SET_NO_STATEMENT_FUNCTION_CALLING == 'False':
                codes4 = code_texted4.replace(function_shape2, prt7)
            else:
                lines = code_texted4.strip().split("\n")
                for i in range(len(lines)):
                    for short, full in func_mapping_var:
                        lines[i] = lines[i].replace(short, full)
                codes4 = "\n".join(lines)
        if f'{b[-5]}{goto4}{b[-8]}' in code_texted4:
            if SET_NO_STATEMENT_FUNCTION_CALLING == 'False':
                codes4 = code_texted4.replace(f'{b[-5]}{goto4}{b[-8]}', prt8)
            else:
                lines = code_texted4.strip().split("\n")
                for i in range(len(lines)):
                    for short, full in func_mapping_var:
                        lines[i] = lines[i].replace(short, full)
                codes4 = "\n".join(lines)
        else:
            if SET_NO_STATEMENT_FUNCTION_CALLING == 'False':
                codes4 = code_texted4.replace(em_function_shape2, token_message4)
            else:
                lines = code_texted4.strip().split("\n")
                for i in range(len(lines)):
                    for short, full in func_mapping_var:
                        lines[i] = lines[i].replace(short, full)
                codes4 = "\n".join(lines)
        fin_lines3 = codes4.strip().split("\n")
        codee2 = "\n".join(fin_lines3)
        return codee2
def runner(code:str,programminglanguage:str,CAROCO:int,PRDF:str='',parallelrun:bool=False,showrunmessage:bool=True,showmessageshowingwarnings:bool=False,returned:bool=False,datalogfilename:str=''):
    global programminglanguagefileformat,command,command2
    if programminglanguage == 'data':
        iD = open(datalogfilename,'w')
        iD.write('')
        iD.close()
        DLA = open(datalogfilename,'w')
        DLA.write(code)
        DLA.close()
    if programminglanguage == 'python':
        if parallelrun == True:
            command2 = f'python {PRDF}'
        pass
    if programminglanguage == 'C' or programminglanguage == 'c':
        programminglanguagefileformat = '.c'
        if CAROCO == 1:
            command = "gcc runned_code.c & a.exe"
        if CAROCO == 2:
            command = "gcc runned_code.c"
        if CAROCO == 1 and parallelrun == True:
            command2 = f'gcc {PRDF} & a.exe'
        if CAROCO == 2 and parallelrun == True:
            command2 = "gcc runned_code.c"
        if CAROCO != 1 and CAROCO != 2:
            print('the value of CAROCO perimeter it is out of range or is not a integer value')
            exit()
    if programminglanguage == 'batch':
        programminglanguagefileformat = '.bat'
        command = "runned_code.bat"
        if parallelrun == True:
            command2 = f'{PRDF}'
    if programminglanguage == 'java':
        programminglanguagefileformat = '.java'
        command = "java runned_code.java"
        if parallelrun == True:
            command2 = f"java {PRDF}"
    if programminglanguage == 'javascript' or programminglanguage == 'JS':
        programminglanguagefileformat = '.js'
        command = "node runned_code.js"
        if parallelrun == True:
            command2 = f"node {PRDF}"
    if programminglanguage == 'html':
        programminglanguagefileformat = '.html'
        command = "runned_code.html"
        if parallelrun == True:
            command2 = f"{PRDF}"
    if programminglanguage == 'kotlin':
        programminglanguagefileformat = '.kt'
        if CAROCO == 1:
            command = "kotlinc runned_code.kt & kotlin Runned_codeKT.class"
            if parallelrun == True:
                data = PRDF
                data1 = data
                data2 = data1[0].upper() + data1[1:]
                data3 = data2[:-3] + data2[-2].upper() + data2[-1].upper()
                command2 = f"kotlinc {data1} & kotlin {data3}.class"
                print(command2)
        if CAROCO == 2:
            command = "kotlinc runned_code.kt"
            if parallelrun == True:
                command2 = f"kotlinc {PRDF}"
        if CAROCO != 1 and CAROCO != 2:
            print('the value of CAROCO perimeter it is out of range or is not a integer value')
            exit()
    if programminglanguage != 'data':
        with open(f"runned_code{programminglanguagefileformat}", "w") as file:
            file.write(f'{code}')
        if parallelrun == True:
            with open(f"{PRDF}", "w") as file2:
                file2.write('')
            with open(f"{PRDF}", "w") as file:
                file.write(f'{code}')
            os.system(f'start cmd /k {command2}')
        else:
            subprocess.Popen(command, shell=True).wait()

        y = int(time.strftime('%Y%d%d%H%M%S'))

        end_time = time.time()
        time_diff = end_time - start_time
        if parallelrun == True and showrunmessage == True:
            os.system(f"echo the {PRDF} file running by using parallel run🔥")
        if parallelrun == False and showrunmessage == True:
            print('note:running more than normal run like the all run_pre or else make the compiler')
            print('shows the run time is add to the run time before it')
            print(f"{programminglanguage.upper()} Finished in {time_diff:.3f} seconds")
        if showmessageshowingwarnings == True and parallelrun == True and showrunmessage == True:
            print('if the terminal or any another way to show the run message and you run the code')
            print('by using parallel run you could found |?|')
            print('this is because your terminal cannot show emojis (flame emoji)')
        if returned == True:
            fooe = open("run_system_functions_AOC.txt", 'w')
            fooe.write(code)
SET_NO_STATEMENT_FUNCTION_CALLING = list_to_string(find_between2(options, '$<set no statement function calling>','/set no statement function calling>$', 1))
def run(programminglanguage:str,CAROCO:int, runned:bool, returned:bool, file_path:str='', thecode:str='', PRDF:str='', Parallelrun:bool=False, showrunmessage:bool=True, showmessageshowingwarnings:bool=False,datalogfilename:str=''):
    func_mapping_var = {}
    fl = open('run_system_functions_AOC.txt','w')
    fl.write('')
    fl.close()
    if programminglanguage == 'python':
        func_mapping_var = PAPFL.func_mapping.keys()
    if programminglanguage == 'C' or programminglanguage == 'c':
        func_mapping_var = CAPFL.func_mapping.keys()
    if programminglanguage == 'java':
        func_mapping_var = JAPFL.func_mapping.keys()
    if programminglanguage == 'javascript' or programminglanguage == 'JS':
        func_mapping_var = JSAPFL.func_mapping.keys()
    if programminglanguage == 'batch':
        func_mapping_var = BAPFL.func_mapping.keys()
    if programminglanguage == 'kotlin':
        func_mapping_var = KTAPFL.func_mapping.keys()
    if programminglanguage == 'html':
        func_mapping_var = HAPFL.func_mapping.keys()
    if programminglanguage != 'python' and programminglanguage != 'C' and programminglanguage != 'c'and programminglanguage != 'java' and programminglanguage != 'javascript' and programminglanguage != 'JS' and programminglanguage != 'batch' and programminglanguage != 'kotlin' and programminglanguage != 'html' and programminglanguage != 'data':
        print("unknown programming language")
        exit()
    if file_path != '':
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                code1 = f.read()
                for i in range(100000):
                    if programminglanguage != 'all' and f'<{programminglanguage} part s>{i + 1}' in code1:
                            code2 = list_to_string2(find_between2_2(code1,f'<{programminglanguage} part s>{i + 1}', f'<{programminglanguage} part e>{i + 1}', 1))
                            py = open('run_system_functions_AOC.txt', 'a')
                            print(code2, file=py)
                            py.close()
                global start_time,command2,command,token_message,token_message2,token_message3,token_message4,programminglanguagefileformat,func_mapping_var2,options,SET_NO_STATEMENT_FUNCTION_CALLING
                codeh = open('run_system_functions_AOC.txt', 'r')
                helpercode = codeh.read()
                codeh.close()
                x = int(time.strftime('%Y%d%d%H%M%S'))
                code = compile('c','',helpercode,programminglanguage)
                if returned == True and runned == False:
                    return code
                if runned == True and returned == True:
                    runner(code,programminglanguage,CAROCO,PRDF,Parallelrun,showrunmessage,showmessageshowingwarnings,returned,datalogfilename) # type: ignore
                    return code
                if runned == True and returned == False:
                    runner(code,programminglanguage,CAROCO,PRDF,Parallelrun,showrunmessage,showmessageshowingwarnings,returned,datalogfilename) # type: ignore
        else:
            print(f"The file '{file_path}' does not exist")
    else:
        for i in range(100000):
            if f'<{programminglanguage} part s>{i + 1}' in thecode:
                code1 = list_to_string2(find_between2(thecode, f'<{programminglanguage} part s>{i + 1}',f'<{programminglanguage} part e>{i + 1}', 1))
                py = open('run_system_functions_AOC.txt', 'a')
                print(code1, file=py)
                py.close()
        global start_time,command2,command,token_message,token_message2,token_message3,token_message4,programminglanguagefileformat,func_mapping_var2,options,SET_NO_STATEMENT_FUNCTION_CALLING
        codeh = open('run_system_functions_AOC.txt', 'r')
        helpercode = codeh.read()
        codeh.close()
        x = int(time.strftime('%Y%d%d%H%M%S'))
        code = compile('c','',helpercode,programminglanguage)
        if returned == True and runned == False:
            return code
        if runned == True and returned == True:
            runner(code,programminglanguage,CAROCO,PRDF,Parallelrun,showrunmessage,showmessageshowingwarnings,returned,datalogfilename) # type: ignore
            return code
        if runned == True and returned == False:
            runner(code,programminglanguage,CAROCO,PRDF,Parallelrun,showrunmessage,showmessageshowingwarnings,returned,datalogfilename) # type: ignore
def parallelrunfilesgen(filename:str,fileformat:str):
    try:
        f = open(f'{filename}_PRDF{fileformat}','x')
    except:
        print("this file already exists")
def GLCfilegenrator(file_name_without_file_format:str,Python_PRDF:bool=False,C_PRDF:bool=False,Java_PRDF:bool=False,JS_PRDF:bool=False,HTML_PRDF:bool=False,Batch_PRDF:bool=False,Kotlin_PRDF:bool=False):
    try:
        ma = open(f'{file_name_without_file_format}.gcf','x')
        ma.close()
    except:
        pass
    if Python_PRDF == True:
        try:
            p1 = open(f'{file_name_without_file_format}_PRDF.py')
        except:
            pass
    if C_PRDF == True:
        try:
            c1 = open(f'{file_name_without_file_format}_PRDF.c')
        except:
            pass
    if Java_PRDF == True:
        try:
            j1 = open(f'{file_name_without_file_format}_PRDF.java')
        except:
            pass
    if JS_PRDF == True:
        try:
            js1 = open(f'{file_name_without_file_format}_PRDF.js')
        except:
            pass
    if HTML_PRDF == True:
        try:
            h1 = open(f'{file_name_without_file_format}_PRDF.html')
        except:
            pass
    if Batch_PRDF == True:
        try:
            b1 = open(f'{file_name_without_file_format}_PRDF.bat')
        except:
            pass
    if Kotlin_PRDF == True:
        try:
            k1 = open(f'{file_name_without_file_format}_PRDF.kt')
        except:
            pass
def GLCfilegenrator2(file_name_without_file_format,Python_PRDF:bool=True,C_PRDF:bool=True,Java_PRDF:bool=True,JS_PRDF:bool=True,HTML_PRDF:bool=True,Batch_PRDF:bool=True,Kotlin_PRDF:bool=True):
    try:
        ma = open(f'{file_name_without_file_format}.gcf','x')
        ma.close()
    except:
        pass
    if Python_PRDF == True:
        try:
            p1 = open(f'{file_name_without_file_format}_PRDF.py')
        except:
            pass
    if C_PRDF == True:
        try:
            c1 = open(f'{file_name_without_file_format}_PRDF.c')
        except:
            pass
    if Java_PRDF == True:
        try:
            j1 = open(f'{file_name_without_file_format}_PRDF.java')
        except:
            pass
    if JS_PRDF == True:
        try:
            js1 = open(f'{file_name_without_file_format}_PRDF.js')
        except:
            pass
    if HTML_PRDF == True:
        try:
            h1 = open(f'{file_name_without_file_format}_PRDF.html')
        except:
            pass
    if Batch_PRDF == True:
        try:
            b1 = open(f'{file_name_without_file_format}_PRDF.bat')
        except:
            pass
    if Kotlin_PRDF == True:
        try:
            k1 = open(f'{file_name_without_file_format}_PRDF.kt')
        except:
            pass