import os
import run_system_functions
class blockfunctions():
    def __init__(self):
        self.blockaddress = 0
        self.filepath = ''
        self.newpath = ''

    def find_between(self, filepath, first_word, second_word, occurrence):
        file = open(filepath, 'r')
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
                second_line_number =i
                break

        if first_line_number is not None and second_line_number is not None:
            words_between = []
            for i in range(first_line_number + 1, second_line_number):
                line = lines[i].strip()
                words_between.append(lines[i])
            return words_between
        else:
            return []  # If either first_word or second_word is not found in the file or occurrence is not found
 
    def pol(self, holder,holderexists,thecode2):
        if holderexists == True:
            theholder2 = open(f'{holder}','w')
            theholder2.write(thecode2)
            theholder2.close()
        if holderexists == False:
            theholder3 = open(f'{holder}','x')
            theholder3.close()
            theholder2 = open(f'{holder}','w')
            theholder2.write(thecode2)
            theholder2.close()
    def find_betweencode(self, code, first_word, second_word,holder,holderexists:bool, occurrence):
        thecode2 = code
        self.pol(holder,holderexists,thecode2)
        theholder = open(holder, 'r')
        lines = theholder.readlines()
        theholder.close()
        delholdd = open(holder,'w')
        delholdd.write('')
        delholdd.close
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

    def find_between3(self, text, firstword, secondword):
        start_index = text.find(firstword) + len(firstword)
        end_index = text.find(secondword)
        if start_index == -1 or end_index == -1:
            return None
        return text[start_index:end_index]
    def list_to_string(self, lst):
        string = ''.join(lst)
        string = string.replace('\\n', '\n')
        return string

    def edit_line(self, file_name, line_number, new_text):
        """Edits the specified line in the given Python file.
        Args:
          file_name: The name of the Python file to edit.
          line_number: The number of the line to edit.
          new_text: The new text to write to the file.
        """
        with open(file_name, "r") as f:
            source_code = f.read()

        lines = source_code.split("\n")
        lines[line_number - 1] = new_text

        with open(file_name, "w") as f:
            f.write("\n".join(lines))

    def pre_makeblock(self, filepath: str, blockinfo: list, where: int, comment: str = None):
        """make block in specific line and file and it create it by using blockinfo that
        is a list the first element is the programming language of block the secound one is
        address of the block"""
        self.filepath = filepath
        self.linenumber = where
        self.comment = comment
        self.blockstarter1 = f'{self.comment}<{blockinfo[0]} part s>{blockinfo[1]}'
        self.blockender1 = f'{self.comment}<{blockinfo[0]} part e>{blockinfo[1]}'
        self.blockstarter = self.blockstarter1
        self.blockender = self.blockender1
        if self.comment == None:
            self.blockstarter = self.blockstarter1[4:]
            self.blockender = self.blockender1[4:]
        if self.comment == 'None':
            self.blockstarter = self.blockstarter1[4:]
            self.blockender = self.blockender1[4:]
        self.edit_line(file_name=self.filepath, line_number=self.linenumber, new_text=f'{self.blockstarter}\n')
        self.edit_line(file_name=self.filepath, line_number=self.linenumber + 1, new_text='\n')
        self.edit_line(file_name=self.filepath, line_number=self.linenumber + 2, new_text=f'{self.blockender}')

    def pre_codeblock(self, filepath: str, blockinfo: list, where: int, code: str, codelines: int, comment: str = None):
        """make block in specific line and file and it create it by using blockinfo that
        is a list the first element is the programming language of block the secound one is
        address of the block"""
        self.filepath = filepath
        self.linenumber = where
        self.comment = comment
        self.blockstarter1 = f'{self.comment}<{blockinfo[0]} part s>{blockinfo[1]}'
        self.blockender1 = f'{self.comment}<{blockinfo[0]} part e>{blockinfo[1]}'
        self.blockstarter = self.blockstarter1
        self.blockender = self.blockender1
        if self.comment == None:
            self.blockstarter = self.blockstarter1[4:]
            self.blockender = self.blockender1[4:]
        if self.comment == 'None':
            self.blockstarter = self.blockstarter1[4:]
            self.blockender = self.blockender1[4:]
        self.edit_line(file_name=self.filepath, line_number=self.linenumber, new_text=f'{self.blockstarter}\n')
        self.edit_line(file_name=self.filepath, line_number=self.linenumber + 1, new_text=f'{code}\n')
        self.edit_line(file_name=self.filepath, line_number=self.linenumber + 2 + codelines,new_text=f'{self.blockender}')

    def blockfile(self, file_name: str, blockinfo: list, datatransferfile: str, datatransferfileformat: str):
        self.filepath = file_name
        self.openedfile = open(self.filepath, 'r')
        self.blockmodule = f'<{blockinfo[0]} part s>{blockinfo[1]}'
        self.blockmodule1 = f'<{blockinfo[0]} part e>{blockinfo[1]}'
        if self.blockmodule in self.openedfile.read():
            self.code1 = self.find_between(self.filepath, self.blockmodule, self.blockmodule1, 1)
            self.code2 = self.list_to_string(self.code1)
            self.pl = open(f'{datatransferfile}{datatransferfileformat}', 'a')
            print(self.code2, file=self.pl)
            self.pl.close()
            self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
    def pre_blockrun(self, file_name: str, blockinfo: list, datatransferfile: str, datatransferfileformat: str, someinfo=None):
        """
        note:this one needs file not code
        note:the data programming language works only by using the someinfo mode
        note:this is the parameters input sequence in the someinfo list
        first one: CAROCO
        second one: returned
        third one: PRDF
        forth one: parallelrun
        fifth one: showrunmessage
        sixth one: showmessageshowingwarnings
        seventh one *: datalogfilename
        *seventh one is optional for only data programming language run
        """
        if someinfo is None:
            someinfo = []
        self.filepath = file_name
        self.openedfile = open(self.filepath, 'r')
        self.blockmodule = f'<{blockinfo[0]} part s>{blockinfo[1]}'
        self.blockmodule1 = f'<{blockinfo[0]} part e>{blockinfo[1]}'
        if self.blockmodule in self.openedfile.read():
            self.code1 = self.find_between(self.filepath, self.blockmodule, self.blockmodule1, 1)
            self.code2 = self.list_to_string(self.code1)
            self.pl = open(f'{datatransferfile}{datatransferfileformat}', 'a')
            print(self.blockmodule, file=self.pl)
            print(self.code2, file=self.pl)
            print(self.blockmodule1, file=self.pl)
            self.pl.close()
            self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
        if someinfo == [] or someinfo is None:
            if blockinfo[0] == 'python':
                run_system_functions.run('python',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'C':
                run_system_functions.run('C',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'java':
                run_system_functions.run('java',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'html':
                run_system_functions.run('html',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'JS':
                run_system_functions.run('JS',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'kotlin':
                run_system_functions.run('kotlin',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'batch':
                run_system_functions.run('batch',1,False,f'{datatransferfile}{datatransferfileformat}')
            self.datatorun.close()
        if someinfo != [] and someinfo is not None:
            if blockinfo[0] == 'python':
                run_system_functions.run('python', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'C':
                run_system_functions.run('C',someinfo[0], someinfo[1],f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'java':
                run_system_functions.run('java', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'html':
                run_system_functions.run('html', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'JS':
                run_system_functions.run('JS', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'kotlin':
                run_system_functions.run('kotlin', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'batch':
                run_system_functions.run('batch', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'data':
                run_system_functions.run('data', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5],someinfo[6])
            self.datatorun.close()
        self.delpl = open(f'{datatransferfile}{datatransferfileformat}','w')
        self.delpl.write('')
        self.delpl.close()
    def pre_blockcoderun(self, code:str,holder, holderexists, blockinfo: list, datatransferfile: str, datatransferfileformat: str, someinfo=None):
        """
        note:this one needs code not file
        note:the data programming language works only by using the someinfo mode
        note:this is the parameters input sequence in the someinfo list
        first one: CAROCO
        second one: returned
        third one: PRDF
        forth one: parallelrun
        fifth one: showrunmessage
        sixth one: showmessageshowingwarnings
        seventh one *: datalogfilename
        *seventh one is optional for only data programming language run
        """
        if someinfo is None:
            someinfo = []
        self.code = code
        self.blockmodule = f'<{blockinfo[0]} part s>{blockinfo[1]}'
        self.blockmodule1 = f'<{blockinfo[0]} part e>{blockinfo[1]}'
        if self.blockmodule in self.code:
            self.code1 = self.find_betweencode(self.code, self.blockmodule, self.blockmodule1, holder, holderexists, 1)
            self.code2 = self.list_to_string(self.code1)
            self.pl = open(f'{datatransferfile}{datatransferfileformat}', 'a')
            print(self.blockmodule, file=self.pl)
            print(self.code2, file=self.pl)
            print(self.blockmodule1, file=self.pl)
            self.pl.close()
            self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
        if someinfo == [] or someinfo is None:
            if blockinfo[0] == 'python':
                run_system_functions.run('python',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'C':
                run_system_functions.run('C',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'java':
                run_system_functions.run('java',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'html':
                run_system_functions.run('html',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'JS':
                run_system_functions.run('JS',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'kotlin':
                run_system_functions.run('kotlin',1,False,f'{datatransferfile}{datatransferfileformat}')
            if blockinfo[0] == 'batch':
                run_system_functions.run('batch',1,False,f'{datatransferfile}{datatransferfileformat}')
            self.datatorun.close()
        if someinfo != [] and someinfo is not None:
            if blockinfo[0] == 'python':
                run_system_functions.run('python', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3],someinfo[4], someinfo[5])
            if blockinfo[0] == 'C':
                run_system_functions.run('C',someinfo[0], someinfo[1],f'{datatransferfile}{datatransferfileformat}','',someinfo[3], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'java':
                run_system_functions.run('java', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'html':
                run_system_functions.run('html', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'JS':
                run_system_functions.run('JS', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'kotlin':
                run_system_functions.run('kotlin', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'batch':
                run_system_functions.run('batch', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
            if blockinfo[0] == 'data':
                run_system_functions.run('data', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5],someinfo[6])
            self.datatorun.close()
        self.delpl = open(f'{datatransferfile}{datatransferfileformat}','w')
        self.delpl.write('')
        self.delpl.close()
    def pre_blockallrun(self, file_name=None, blockinfo_=None, datatransferfile_=None, datatransferfileformat_=None, someinfo_=None):
            """
            note:this one needs file not code
            note:the data programming language works only by using the someinfo_ mode
            note:this is the parameters input sequence in the someinfo list
            first one: CAROCO
            second one: returned
            third one: PRDF
            forth one: parallelrun
            fifth one: showrunmessage
            sixth one: showmessageshowingwarnings
            seventh one *: datalogfilename
            *seventh one is optional for only data programming language run
            """
            if file_name is None:
                file_name = []
            if blockinfo_ is None:
                blockinfo_ = []
            if datatransferfile_ is None:
                datatransferfile_ = []
            if datatransferfileformat_ is None:
                datatransferfileformat_ = []
            if someinfo_ is None:
                someinfo_ = []
            datatransferfile__ = datatransferfile_
            datatransferfileformat__ = datatransferfileformat_
            for i in range(len(file_name)):
                self.filepath = file_name[i]
                if someinfo_ != []:
                    someinfo = someinfo_[i]
                else:
                    someinfo = []
                datatransferfile = datatransferfile__[i]
                datatransferfileformat = datatransferfileformat__[i]
                self.openedfile = open(self.filepath, 'r')
                blockinfo = blockinfo_[i]
                self.blockmodule = f'<{blockinfo[0]} part s>{blockinfo[1]}'
                self.blockmodule1 = f'<{blockinfo[0]} part e>{blockinfo[1]}'
                if self.blockmodule in self.openedfile.read():
                    self.code1 = self.find_between(self.filepath, self.blockmodule, self.blockmodule1, 1)
                    self.code2 = self.list_to_string(self.code1)
                    self.pl = open(f'{datatransferfile}{datatransferfileformat}', 'a')
                    print(self.blockmodule, file=self.pl)
                    print(self.code2, file=self.pl)
                    print(self.blockmodule1, file=self.pl)
                    self.pl.close()
                    self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
                if someinfo == [] or someinfo is None:
                    self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
                    if blockinfo[0] == 'python':
                        run_system_functions.run('python',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'C':
                        run_system_functions.run('C',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'java':
                        run_system_functions.run('java',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'html':
                        run_system_functions.run('html',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'JS':
                        run_system_functions.run('JS',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'kotlin':
                        run_system_functions.run('kotlin',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'batch':
                        run_system_functions.run('batch',1,False,f'{datatransferfile}{datatransferfileformat}')
                    self.datatorun.close()
                if someinfo != [] and someinfo is not None:
                    self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
                    if blockinfo[0] == 'python':
                        run_system_functions.run('python', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'C':
                        run_system_functions.run('C',someinfo[0], someinfo[1],f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0  ] == 'java':
                        run_system_functions.run('java', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'html':
                        run_system_functions.run('html', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'JS':
                        run_system_functions.run('JS', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'kotlin':
                        run_system_functions.run('kotlin', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'batch':
                        run_system_functions.run('batch', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'data':
                        run_system_functions.run('data', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5],someinfo[6])
                    self.datatorun.close()
                self.delpl = open(f'{datatransferfile}{datatransferfileformat}','w')
                self.delpl.write('')
                self.delpl.close()
    def pre_blockcodeallrun(self, code_=None, holder_=None, holderexists_=None, blockinfo_=None, datatransferfile_=None, datatransferfileformat_=None, someinfo_=None):
            """
            note:this one needs code not file
            note:the data programming language works only by using the someinfo mode
            note:this is the parameters input sequence in the someinfo list
            first one: CAROCO
            second one: returned
            third one: PRDF
            forth one: parallelrun
            fifth one: showrunmessage
            sixth one: showmessageshowingwarnings
            seventh one *: datalogfilename
            *seventh one is optional for only data programming language run
            """
            if code_ is None:
                code_ = []
            if blockinfo_ is None:
                blockinfo_ = []
            if holder_ is None:
                holder_ = []
            if holderexists_ is None:
                holderexists_ = []
            if datatransferfile_ is None:
                datatransferfile_ = []
            if datatransferfileformat_ is None:
                datatransferfileformat_ = []
            if someinfo_ is None:
                someinfo_ = []
            datatransferfile__ = datatransferfile_
            datatransferfileformat__ = datatransferfileformat_
            for i in range(len(holderexists_)):
                self.code = code_[i]
                if someinfo_ != []:
                    someinfo = someinfo_[i]
                else:
                    someinfo = []
                holder = holder_[i]
                holderexists = holderexists_[i]
                datatransferfile = datatransferfile__[i]
                datatransferfileformat = datatransferfileformat__[i]
                blockinfo = blockinfo_[i]
                self.blockmodule = f'<{blockinfo[0]} part s>{blockinfo[1]}'
                self.blockmodule1 = f'<{blockinfo[0]} part e>{blockinfo[1]}'
                if self.blockmodule in self.code:
                    self.code1 = self.find_betweencode(self.code, self.blockmodule, self.blockmodule1, holder, holderexists, 1)
                    self.code2 = self.list_to_string(self.code1)
                    self.pl = open(f'{datatransferfile}{datatransferfileformat}', 'a')
                    print(self.blockmodule, file=self.pl)
                    print(self.code2, file=self.pl)
                    print(self.blockmodule1, file=self.pl)
                    self.pl.close()
                    self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
                if someinfo == [] or someinfo is None:
                    self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
                    if blockinfo[0] == 'python':
                        run_system_functions.run('python',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'C':
                        run_system_functions.run('C',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'java':
                        run_system_functions.run('java',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'html':
                        run_system_functions.run('html',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'JS':
                        run_system_functions.run('JS',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'kotlin':
                        run_system_functions.run('kotlin',1,False,f'{datatransferfile}{datatransferfileformat}')
                    if blockinfo[0] == 'batch':
                        run_system_functions.run('batch',1,False,f'{datatransferfile}{datatransferfileformat}')
                    self.datatorun.close()
                if someinfo != [] and someinfo is not None:
                    self.datatorun = open(f'{datatransferfile}{datatransferfileformat}', 'r')
                    if blockinfo[0] == 'python':
                        run_system_functions.run('python', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'C':
                        run_system_functions.run('C',someinfo[0], someinfo[1],f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0  ] == 'java':
                        run_system_functions.run('java', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'html':
                        run_system_functions.run('html', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'JS':
                        run_system_functions.run('JS', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'kotlin':
                        run_system_functions.run('kotlin', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'batch':
                        run_system_functions.run('batch', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5])
                    if blockinfo[0] == 'data':
                        run_system_functions.run('data', someinfo[0], someinfo[1], f'{datatransferfile}{datatransferfileformat}','', someinfo[2], someinfo[3], someinfo[4], someinfo[5],someinfo[6])
                    self.datatorun.close()
                self.delpl = open(f'{datatransferfile}{datatransferfileformat}','w')
                self.delpl.write('')
                self.delpl.close()
blockclass = blockfunctions()