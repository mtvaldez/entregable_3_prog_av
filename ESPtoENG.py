import ply.lex as lex
from Validator import validator

reserved = {
    "TRAEME": "SELECT",
    "TODO": "STAR",  
    "DE LA TABLA": "FROM",  # 0
    "DONDE": "WHERE",
    "AGRUPANDO POR": "GROUP_BY",  # 1
    "MEZCLANDO": "JOIN",
    "EN": "ON",
    "LOS DISTINTOS": "DISTINCT",  # 2
    "CONTANDO": "COUNT",
    "METE EN": "INSERT_INTO",  # 3
    "LOS VALORES": "VALUES",  # 4
    "ACTUALIZA": "UPDATE",
    "SETEA": "SET",
    "BORRA DE LA": "DELETE_FROM",  # 5
    "ORDENA POR": "ORDER_BY",  # 6
    "COMO MUCHO": "LIMIT",  # 7
    "WHERE DEL GROUP BY": "HAVING",  # 8
    "EXISTE": "EXISTS",
    "EN ESTO:": "IN",  # 9
    "ENTRE": "BETWEEN",
    "PARECIDO A": "LIKE",  # 10
    "ES NULO": "IS_NULL",  # 11
    "CAMBIA LA TABLA": "ALTER_TABLE",  # 12
    "AGREGA LA COLUMNA": "ADD_COLUMN",  # 13
    "ELIMINA LA COLUMNA": "DROP_COLUMN",  # 14
    "CREA LA TABLA": "CREATE_TABLE",  # 15
    "TIRA LA TABLA": "DROP_TABLE",  # 16
    "POR DEFECTO": "DEFAULT",  # 17
    "UNICO": "UNIQUE",
    "CLAVE PRIMA": "PRIMARY_KEY",  # 18
    "CLAVE REFERENTE": "FOREIGN_KEY",  # 19
    "NO NULO": "NOT_NULL",  # 20
    "TRANSFORMA A": "CAST",  # 21
    "Y":"AND"
}

tokens = [
    'IDENTIFIER', 'COMMA', 'EQUALS', 'NUMBER', 'STRING', 'LPAREN', 'RPAREN'
] + list(reserved.values())

def t_FROM(t):
    r'DE\s+LA\s+TABLA'
    t.type = 'FROM'
    return t

def t_GROUP_BY(t):
    r'AGRUPANDO\s+POR'
    t.type = 'GROUP_BY'
    return t

def t_DISTINCT(t):
    r'LOS\s+DISTINTOS'
    t.type = 'DISTINCT'
    return t

def t_INSERT_INTO(t):
    r'METE\s+EN'
    t.type = 'INSERT_INTO'
    return t

def t_VALUES(t):
    r'LOS\s+VALORES'
    t.type = 'VALUES'
    return t

def t_DELETE_FROM(t):
    r'BORRA\s+DE\s+LA'
    t.type = 'DELETE_FROM'
    return t

def t_ORDER_BY(t):
    r'ORDENA\s+POR'
    t.type = 'ORDER_BY'
    return t

def t_LIMIT(t):
    r'COMO\s+MUCHO'
    t.type = 'LIMIT'
    return t

def t_HAVING(t):
    r'WHERE\s+DEL\s+GROUP\s+BY'
    t.type = 'HAVING'
    return t

def t_IN(t):
    r'EN\s+ESTO:'
    t.type = 'IN'
    return t

def t_LIKE(t):
    r'PARECIDO\s+A'
    t.type = 'LIKE'
    return t

def t_IS_NULL(t):
    r'ES\s+NULO'
    t.type = 'IS_NULL'
    return t

def t_ALTER_TABLE(t):
    r'CAMBIA\s+LA\s+TABLA'
    t.type = 'ALTER_TABLE'
    return t

def t_ADD_COLUMN(t):
    r'AGREGA\s+LA\s+COLUMNA'
    t.type = 'ADD_COLUMN'
    return t

def t_DROP_COLUMN(t):
    r'ELIMINA\s+LA\s+COLUMNA'
    t.type = 'DROP_COLUMN'
    return t

def t_CREATE_TABLE(t):
    r'CREA\s+LA\s+TABLA'
    t.type = 'CREATE_TABLE'
    return t

def t_DROP_TABLE(t):
    r'TIRA\s+LA\s+TABLA'
    t.type = 'DROP_TABLE'
    return t

def t_DEFAULT(t):
    r'POR\s+DEFECTO'
    t.type = 'DEFAULT'
    return t

def t_PRIMARY_KEY(t):
    r'CLAVE\s+PRIMA'
    t.type = 'PRIMARY_KEY'
    return t

def t_FOREIGN_KEY(t):
    r'CLAVE\s+REFERENTE'
    t.type = 'FOREIGN_KEY'
    return t

def t_NOT_NULL(t):
    r'NO\s+NULO'
    t.type = 'NOT_NULL'
    return t

def t_CAST(t):
    r'TRANSFORMA\s+A'
    t.type = 'CAST'
    return t

t_COMMA = r','
t_EQUALS = r'='
t_STRING = r"'[^']*'"
t_NUMBER = r'\d+'
t_LPAREN = r'\(' 
t_RPAREN = r'\)' 

t_ignore = ' \t\n'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    usql_value = t.value.upper()
    t.type = reserved.get(usql_value, 'IDENTIFIER')
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    data = input("Ingrese query:\n")
    lexer.input(data)
    # TRAEME nombre DE LA TABLA empleados DONDE EXISTE (TRAEME 1 DE LA TABLA proyectos DONDE id = departamento_id)
    sql_query = ""
    for tok in lexer:
        sql_query += tok.value + " " if (tok.type in ['IDENTIFIER', 'COMMA', 'EQUALS', 'NUMBER', 'STRING', 'LPAREN', 'RPAREN']) else tok.type.replace('_', ' ')   + " "
    print(sql_query+"\n")
    validator.validate_sql_syntax(sql_query)