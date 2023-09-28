import block_fun
blockclass = block_fun.blockfunctions()
def pre_blockmake(filepath:str,blocklist:list,put_in:int,comment:str = None):
    blockclass.pre_makeblock(filepath, blocklist, put_in, comment)
def precodeblock(filepath:str,blocklist:list,put_in:int, code:str,codelines:int,comment:str = None):
    blockclass.pre_codeblock(filepath, blocklist, put_in,code,codelines, comment)
def fileblock(file_name:str, blockinfo:list, datatransferfile:str,datatransferfileformat:str):
    blockclass.blockfile(file_name,blockinfo,datatransferfile,datatransferfileformat)
def pre_blockrun(file_name:str, blockinfo:list, datatransferfile:str,datatransferfileformat:str, someinfo=None):
    if someinfo is None:
        someinfo = []
    blockclass.pre_blockrun(file_name, blockinfo, datatransferfile,datatransferfileformat,someinfo)