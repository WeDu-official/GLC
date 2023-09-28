from ply import lex, yacc
#the comments at here are recommend places to write code that is about them
#note you can write your code anywhere my comments don't matter
#lexer
#put your tokens at here
tokens = ('NUMBER','example')
#make values for your tokens(string way)
t_example = r'\+'
#make values for your tokens(fucntion way)
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Integer value too large: {t.value}")
        t.value = 0
    return t

def t_newlineexample(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#make error handling functions at here
def t_error(t):
    print(f"Illegal character {t.value[0]!r} on line {t.lexer.lineno}")
    t.lexer.skip(1)
#other
t_ignore = ' \t'
#calling the lexer
lexer = lex.lex()
#parser
#parser roles
#make you functions at here
def p_expression_binop(t):
    '''expression : expression example expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
def p_expression_numberexample(t):
    'expression : NUMBER'
    t[0] = t[1]
#make error handling functions at here
def p_error(t):
    if t is None:
        return
    print(f"Syntax Error: {t.value!r}")
#other
#calling the parser
parser = yacc.yacc()