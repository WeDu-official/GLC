import run_system_functions
class file():
    def runfile(self,filepath:str):
        run_system_functions.run('html', 1, False,filepath,'')
    def conv(self,code,mode,fscn):
        if mode == 'c':
            x = run_system_functions.run('html', 1, False, '', code)
            print(x)
        if mode == 'cf':
            x = run_system_functions.run('html', 1, False, '', code)
            w_fscn = open(fscn,'w')
            w_fscn.write(x)
        if mode == 'f':
            with open(fscn, 'r') as f:
                code = f.read()
            x = run_system_functions.run('html', 1, False, '', code)
            print(x)
        if mode == 'ff':
            with open(fscn, 'r') as f:
                code = f.read()
            x = run_system_functions.run('html', 1, False, '', code)
            w_fscn = open(fscn,'w')
            w_fscn.write(x)