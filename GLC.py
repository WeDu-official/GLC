import argparse
import GLClang
import shortcutfunc
import os
parser = argparse.ArgumentParser(description="""this is GLC commander and you can give GLC by using it operations to do like run or convert.""")
parser.add_argument("mode", metavar="MODE", type=str, help="""the mode that of command that you will use them
like r that will give you the runner functions or b that give you the block function""")
parser.add_argument("command", metavar="COMMAND", type=str, help="""the command that you want to do
like run or convert""")
parser.add_argument("commandpri1", metavar="COMMAND_perimeters1", type=str, help="""the perimeter that the command need it to
work""")
parser.add_argument("commandpri2", metavar="COMMAND_perimeters2", type=str, help="""the perimeter that the command need it to
work""")
parser.add_argument("commandpri3", metavar="COMMAND_perimeters3", type=str, help="""the perimeter that the command need it to
work""")
parser.add_argument("commandpri4", metavar="COMMAND_perimeters4", type=str, help="""the perimeter that the command need it to
work""")
args = parser.parse_args()
mode = args.mode
command = args.command
if mode == 'r':
    if command == 'run':
        GLClang.basicrun_pre(args.commandpri1,args.commandpri2,args.commandpri3,args.commandpri4)
    if command == 'runblock':
        num = 2
        elementlist = []
        for i in range(num):
            if i == 0:
                element = input(f'write perimeter the block info {i + 1} element: ')
                elementlist.append(element)
                element2 = input(f'write perimeter the someinfo {i + 1} element: ')
                elementlist.append(element2)
            if i == 1:
                element1 = int(input(f'write perimeter the block info {i + 1} element: '))
                elementlist.append(element1)
                element3 = input(f'write perimeter the someinfo {i + 1} element: ')
                elementlist.append(element3)
        shortcutfunc.pre_blockrun(args.commandpri1,elementlist,args.commandpri3,args.commandpri4)
if mode == 'b':
    if command == 'makeblock':
        num = 2
        elementlist = []
        for i in range(num):
            if i == 0:
                element = input(f'write perimeter the block info {i + 1} element: ')
                elementlist.append(element)
            if i == 1:
                element1 = int(input(f'write perimeter the block info {i + 1} element: '))
                elementlist.append(element1)
        shortcutfunc.pre_blockmake(args.commandpri1,elementlist,int(args.commandpri3),args.commandpri4)
    if command == 'codeblock':
        k = input('''write the code filepath at here: ''')
        j = int(input('how many lines of code in the code filepath: '))
        g = open(k,'r')
        num = 2
        elementlist = []
        for i in range(num):
            if i == 0:
                element = input(f'write perimeter the block info {i + 1} element: ')
                elementlist.append(element)
            if i == 1:
                element1 = int(input(f'write perimeter the block info {i + 1} element: '))
                elementlist.append(element1)
        shortcutfunc.precodeblock(args.commandpri1,elementlist,int(args.commandpri3),g.read(),j,args.commandpri4)
    if command == 'fileblock':
        num = 2
        elementlist = []
        for i in range(num):
            if i == 0:
                element = input(f'write perimeter the block info {i + 1} element: ')
                elementlist.append(element)
            if i == 1:
                element1 = int(input(f'write perimeter the block info {i + 1} element: '))
                elementlist.append(element1)
        shortcutfunc.fileblock(args.commandpri1,elementlist,args.commandpri3,args.commandpri4)
    
if mode == 'op':
    if command == 'clear':
        GLClang.clear_pre(args.commandpri1)
    if command == 'restart':
        GLClang.restart_pre(args.commandpri1)
    if command == 'readdata':
        GLClang.readdata_pre(args.commandpri1,args.commandpri2)
    if command == 'writedata':
        GLClang.writedata_pre(args.commandpri1,args.commandpri2)
    if command == 'clearall':
        GLClang.clearall_pre(args.commandpri1,args.commandpri2)
    if command == 'parallel_run':
        commandpriw1 = ''
        commandpriw2 = ''
        file_path = ''
        code = ''
        PRDF = ''
        Parallelrun = False
        showrunmessage = True
        show_message_showing_warnings = False
        def thebool(thevar):
            if thevar == 'True':
                return True
            if thevar == 'False':
                return False
            else:
                return f'error with {thevar}'
        if int(args.commandpri1) == 0 or int(args.commandpri1) == 1 or int(args.commandpri1) == 2 or int(args.commandpri1) == 3:
            commandpriw1 = input('write the programming language name> ')
            commandpriw2 = input('write if CAROCO must to be 1 or 2> ')
            if args.commandpri2 == 'f':
                file_path = input('write the filepath> ')
            if args.commandpri2 == 'c':
                code = input('write the code> ')
            else:
                print('error')
        if int(args.commandpri1) == 4:
            commandpriw1 = input('write the programming language name> ')
            commandpriw2 = input('write if CAROCO must to be 1 or 2> ')
            if args.commandpri2 == 'f':
                file_path = input('write the filepath> ')
                PRDF = input('write the PRDF> ')
            if args.commandpri2 == 'c':
                code = input('write the code> ')
                PRDF = input('write the PRDF> ')
            else:
                print('error')
        if int(args.commandpri1) == 5:
            commandpriw1 = input('write the programming language name> ')
            commandpriw2 = input('write if CAROCO must to be 1 or 2> ')
            if args.commandpri2 == 'f':
                file_path = input('write the filepath> ')
                PRDF = input('write the PRDF> ')
                Parallelrun = thebool(input('write if parallel run is True or False> '))
            if args.commandpri2 == 'c':
                code = input('write the code> ')
                PRDF = input('write the PRDF> ')
                Parallelrun = thebool(input('write if parallel run is True or False> '))
            else:
                print('error')
        if int(args.commandpri1) == 6:
            commandpriw1 = input('write the programming language name> ')
            commandpriw2 = input('write if CAROCO must to be 1 or 2> ')
            if args.commandpri2 == 'f':
                file_path = input('write the filepath> ')
                PRDF = input('write the PRDF> ')
                Parallelrun = thebool(input('write if parallel run is True or False> '))
                showrunmessage = thebool(input('write if show_run_message is True or False> '))
            if args.commandpri2 == 'c':
                code = input('write the code> ')
                PRDF = input('write the PRDF> ')
                Parallelrun = thebool(input('write if parallel run is True or False> '))
                showrunmessage = thebool(input('write if show_run_message is True or False> '))
            else:
                print('error')
        if int(args.commandpri1) >= 7:
            commandpriw1 = input('write the programming language name> ')
            commandpriw2 = input('write if CAROCO must to be 1 or 2> ')
            if args.commandpri2 == 'f':
                file_path = input('write the filepath> ')
                PRDF = input('write the PRDF> ')
                Parallelrun = thebool(input('write if parallel run is True or False> '))
                showrunmessage = thebool(input('write if show_run_message is True or False> '))
                show_message_showing_warnings = thebool(input('write if show_message_showing_warnings is True or False> '))
            if args.commandpri2 == 'c':
                code = input('write the code> ')
                PRDF = input('write the PRDF> ')
                Parallelrun = thebool(input('write if parallel run is True or False> '))
                showrunmessage = thebool(input('write if show_run_message is True or False> '))
                show_message_showing_warnings = thebool(input('write if show_message_showing_warnings is True or False> '))
            else:
                print('error')
        the_bool = thebool(args.commandpri3)
        the_bool2 = thebool(args.commandpri4)
        GLClang.parallelrun(commandpriw1,int(commandpriw2),the_bool,the_bool2,file_path,code,PRDF,Parallelrun,showrunmessage,show_message_showing_warnings)
    if command == 'run_code':
        data = args.commandpri1
        if '.py' in data:
            os.system(f'python {data}')
        if '.c_compile' in data:
            data1 = data[:-8]
            os.system(f'gcc {data1}')
        if '.c_run' in data:
            data1 = data[:-4]
            os.system(f'gcc {data1} & a.exe')
        if '.c_r_compiled' in data:
            os.system('a.exe')
        if '.java' in data:
            os.system(f'java {data}')
        if '.kt_compile' in data:
            data1 = data[:-8]
            os.system(f'kotlinc {data1}')
        if '.kt_run' in data:
            data1 = data[:-4]
            data2 = data1[0].upper() + data1[1:]
            data3 = data2[:-2] + data2[-2:].upper()
            data4 = data3[:-3] + data3[-2:].upper()
            os.system(f'kotlinc {data1} & kotlin {data4}.class')
        if '.kt_r_compiled' in data:
            data1 = data[:-11]
            data2 = data1[0].upper() + data1[1:]
            data3 = data2[:-2] + data2[-2:].upper()
            data4 = data3[:-3] + data3[-2:].upper()
            os.system(f"kotlin {data4}.class")
        if '.bat' in data:
            os.system(f"{data}")
        if '.js' in data:
            os.system(f"node {data}")
        if '.html' in data:
            os.system(f"{data}")