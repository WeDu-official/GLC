from run_system_functions import *
#create functions
def writedata_pre(readenfile, writeenfile):
    """this function reads readenfile and writes the data of the readenfile
    in writenfile(this function copy the data in readenfile and paste it in writeenfile)."""
    with open(f'{readenfile}', 'r') as la2:
        x = la2.read()
    with open(f'{writeenfile}', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def readdata_pre(readenfile, writeenfile):
    """this function reads readenfile and writes the data of the readenfile
        in writeenfile(this function copy the data in readenfile and paste it in writeenfile)."""
    with open(f'{readenfile}', 'r') as la2:
        x = la2.read()
    with open(f'{writeenfile}', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def clearall_pre(file1,file2):
    """this function clear all data of file1 and file2"""
    with open(f'{file1}', 'w') as la2:
        la2.write('')
    with open(f'{file2}', 'w') as la:
        la.write('')
    la.close()
    la2.close()
def clear_pre(file):
    """this function clear all data of file1"""
    with open(f'{file}', 'w') as la:
        la.write('')
    la.close()
def writedata():
    """this function reads main.gcf or main.PLFF and writes the data of the main.gcf or main.PLFF
        in lacodeasavea.txt(this function copy the data in main.gcf or main.PLFF and paste it in lacodeasavea.txt)."""
    with open('main.gcf', 'r') as la2:
        x = la2.read()
    with open('lacodeasavea.txt', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def readdata():
    """this function reads lacodeasavea.txt and writes the data of the lacodeasavea
            in main.gcf or main.PLFF (this function copy the data in lacodeasavea.txt and paste it in main.gcf or main.PLFF)."""
    with open('lacodeasavea.txt', 'r') as la2:
        x = la2.read()
    with open('main.gcf', 'w') as la:
        la.write(f'{x}')
    la.close()
    la2.close()
def clearall():
    """this function clear all data of lacodeasavea.txt and main.gcf or main.PLFF"""
    with open('lacodeasavea.txt', 'w') as la2:
        la2.write('')
    with open('main.gcf', 'w') as la:
        la.write('')
    la.close()
    la2.close()
def clear1():
    """this function clear all data of main.gcf or main.PLFF"""
    with open('main.gcf', 'w') as la:
        la.write('')
    la.close()
def clear2():
    """this function clear all data of lacodeasavea.txt"""
    with open('lacodeasavea.txt', 'w') as la2:
        la2.write('')
    la2.close()
def run_pre(filename:str,CAROCO:int,programminglanguage:str,datalogfilename:str=''):
    run(programminglanguage,CAROCO,False,filename,'','',False,True,False,datalogfilename)
def allrun_pre(filename=None,CAROCO=None,runorder=None,datalogfilename=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if filename is None: filename = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],False,filename[i],'',datalogfilename=datalogfilename[i])
def allparallelrun_pre(filename=None,CAROCO=None,PRDF=None,runorder=None,datalogfilename=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if PRDF is None: PRDF = []
    if filename is None: filename = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],False,filename[i],'',PRDF[i],True,True,False,datalogfilename=datalogfilename[i])
def run_precode(code:str,CAROCO:int,programminglanguage:str,datalogfilename:str=''):
    run(programminglanguage,CAROCO,False,'',code,'',False,True,False,datalogfilename=datalogfilename)
def allrun_precode(code=None,datalogfilename=None,CAROCO=None,runorder=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if code is None: code = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],False,'',code[i],datalogfilename=datalogfilename[i])
def allparallelrun_precode(code=None,CAROCO=None,PRDF=None,runorder=None,datalogfilename=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if PRDF is None: PRDF = []
    if code is None: code = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],False,'',code[i],PRDF[i],True,True,False,datalogfilename=datalogfilename[i])
def run_precos(programminglanguage:str,filename:str,CAROCO:int,returned:bool,showrunmessage:bool,showmessageswithwarnings:bool,datalogfilename:str=''):
    run(programminglanguage,CAROCO,returned,filename,'','',False,showrunmessage,showmessageswithwarnings,datalogfilename=datalogfilename)
def allrun_precos(filename=None,CAROCO=None,returned=None,showrunmessage=None,showmessageswithwarnings=None,runorder=None,datalogfilename=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if returned is None: returned = []
    if showrunmessage is None: showrunmessage = []
    if showmessageswithwarnings is None: showmessageswithwarnings = []
    if filename is None: filename = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],returned[i],filename[i],'','',False,showrunmessage[i],showmessageswithwarnings[i],datalogfilename=datalogfilename[i])
def allparallelrun_precos(filename=None,datalogfilename=None,CAROCO=None,returned=None,showrunmessage=None,showmessageswithwarnings=None,PRDF=None,runorder=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if returned is None: returned = []
    if showrunmessage is None: showrunmessage = []
    if showmessageswithwarnings is None: showmessageswithwarnings = []
    if PRDF is None: PRDF = []
    if filename is None: filename = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],returned[i],filename[i],'',PRDF[i],True,showrunmessage[i],showmessageswithwarnings[i],datalogfilename=datalogfilename[i])
def run_precodecos(programminglanguage:str,code:str,CAROCO:int,returned:bool,showrunmessage:bool,showmessageswithwarnings:bool,datalogfilename:str=''):
    run(programminglanguage,CAROCO,returned,'',code,'',False,showrunmessage,showmessageswithwarnings,datalogfilename=datalogfilename)
def allrun_precodecos(code=None,CAROCO=None,returned=None,showrunmessage=None,showmessageswithwarnings=None,runorder=None,datalogfilename=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if returned is None: returned = []
    if showrunmessage is None: showrunmessage = []
    if showmessageswithwarnings is None: showmessageswithwarnings = []
    if code is None: code = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],returned[i],'',code[i],'',False,showrunmessage[i],showmessageswithwarnings[i],datalogfilename=datalogfilename[i])
def allparallelrun_precodecos(code=None,CAROCO=None,returned=None,showrunmessage=None,showmessageswithwarnings=None,PRDF=None,runorder=None,datalogfilename=None):
    if runorder is None: runorder = []
    if CAROCO is None: CAROCO = []
    if returned is None: returned = []
    if showrunmessage is None: showrunmessage = []
    if showmessageswithwarnings is None: showmessageswithwarnings = []
    if PRDF is None: PRDF = []
    if code is None: code = []
    if datalogfilename is None: datalogfilename = []
    for i in range(len(runorder)):
        run(runorder[i],CAROCO[i],returned[i],'',code[i],PRDF[i],True,showrunmessage[i],showmessageswithwarnings[i],datalogfilename=datalogfilename[i])
def parallelrun(programminglanguage:str,CAROCO:int,returned:bool,file_path:str='',PRDF:str='',showrunmessage:bool=True,showmessageshowingwarnings:bool=False,datalogfilename:str=''):
    run(programminglanguage,CAROCO,returned,file_path,'',PRDF,True,showrunmessage,showmessageshowingwarnings,datalogfilename=datalogfilename)
def parallelruncode(programminglanguage:str,CAROCO:int,returned:bool,code:str='',PRDF:str='',showrunmessage:bool=True,showmessageshowingwarnings:bool=False,datalogfilename:str=''):
    run(programminglanguage,CAROCO,returned,'',code,PRDF,True,showrunmessage,showmessageshowingwarnings,datalogfilename=datalogfilename)
def parallelrunfilesgenrator(filename:str,fileformat:str):
    parallelrunfilesgen(filename,fileformat)
def GLC_filegenrator(file_name_without_file_format:str,Python_PRDF:bool=False,C_PRDF:bool=False,Java_PRDF:bool=False,JS_PRDF:bool=False,HTML_PRDF:bool=False,Batch_PRDF:bool=False,Kotlin_PRDF:bool=False):
    GLCfilegenrator(file_name_without_file_format,Python_PRDF,C_PRDF,Java_PRDF,JS_PRDF,HTML_PRDF,Batch_PRDF,Kotlin_PRDF)
def GLC_filegenrator2(file_name_without_file_format:str,Python_PRDF:bool=False,C_PRDF:bool=False,Java_PRDF:bool=False,JS_PRDF:bool=False,HTML_PRDF:bool=False,Batch_PRDF:bool=False,Kotlin_PRDF:bool=False):
    GLCfilegenrator2(file_name_without_file_format,Python_PRDF,C_PRDF,Java_PRDF,JS_PRDF,HTML_PRDF,Batch_PRDF,Kotlin_PRDF)
def restart():
    """this function restarts main.gcf or main.PLFF"""
    with open('main.gcf', 'w') as oldb:
        oldb.write('')
def restart_pre(filename):
    """this function restarts filename that is .gcf or .PLFF"""
    with open(f'{filename}', 'w') as oldb:
        oldb.write('') 
def run_code(filename):
    """this function runs code like python files and C files and all other programming
    languages supported by GLC
    note:this function don't compile than by using GLC that means no function mapping
    or things like that it only compile and runs or only compile the file with cmd commands"""
    data = filename
    if '.py' in data:
        os.system(f'python {data}')
    if '.c compile' in data:
        data1 = data[:-8]
        os.system(f'gcc {data1}')
    if '.c run' in data:
        data1 = data[:-4]
        os.system(f'gcc {data1} & a.exe')
    if '.c r_compiled' in data:
        os.system('a.exe')
    if '.java' in data:
        os.system(f'java {data}')
    if '.kt compile' in data:
        data1 = data[:-8]
        os.system(f'kotlinc {data1}')
    if '.kt run' in data:
        data1 = data[:-4]
        data2 = data1[0].upper() + data1[1:]
        data3 = data2[:-2] + data2[-2:].upper()
        data4 = data3[:-3] + data3[-2:].upper()
        os.system(f'kotlinc {data1} & kotlin {data4}.class')
    if '.kt r_compiled' in data:
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