import ply.lex as lex
from Validator import validator

reserved = {
    "SELECT": "TRAEME",
    "FROM": "DE_LA_TABLA",
    "WHERE": "DONDE",
    "GROUP BY": "AGRUPANDO_POR",
    "JOIN": "MEZCLANDO",
    "ON": "EN",
    "DISTINCT": "LOS_DISTINTOS",
    "COUNT": "CONTANDO",
    "INSERT INTO": "METE_EN",
    "VALUES": "LOS_VALORES",
    "UPDATE": "ACTUALIZA",
    "SET": "SETEA",
    "DELETE FROM": "BORRA_DE_LA",
    "ORDER BY": "ORDENA_POR",
    "LIMIT": "COMO_MUCHO",
    "HAVING": "WHERE_DEL_GROUP_BY",
    "EXISTS": "EXISTE",
    "IN": "EN_ESTO",
    "BETWEEN": "ENTRE",
    "LIKE": "PARECIDO_A",
    "IS NULL": "ES_NULO",
    "ALTER TABLE": "CAMBIA_LA_TABLA",
    "ADD COLUMN": "AGREGA_LA_COLUMNA",
    "DROP COLUMN": "ELIMINA_LA_COLUMNA",
    "CREATE TABLE": "CREA_LA_TABLA",
    "DROP TABLE": "TIRA_LA_TABLA",
    "DEFAULT": "POR_DEFECTO",
    "UNIQUE": "UNICO",
    "PRIMARY KEY": "CLAVE_PRIMA",
    "FOREIGN KEY": "CLAVE_REFERENTE",
    "NOT NULL": "NO_NULO",
    "CAST": "TRANSFORMA_A",
    "AND": "Y"
}

tokens = [
    'IDENTIFIER', 'COMMA', 'EQUALS', 'NUMBER', 'STRING', 'LPAREN', 'RPAREN', 'STAR'
] + list(reserved.values())

def t_NO_NULO(t):
    r'NOT\s+NULL'
    t.type = 'NO_NULO'
    return t

def t_AGRUPANDO_POR(t):
    r'GROUP\s+BY'
    t.type = 'AGRUPANDO_POR'
    return t

def t_METE_EN(t):
    r'INSERT\s+INTO'
    t.type = 'METE_EN'
    return t

def t_BORRA_DE_LA(t):
    r'DELETE\s+FROM'
    t.type = 'BORRA_DE_LA'
    return t

def t_ORDENA_POR(t):
    r'ORDER\s+BY'
    t.type = 'ORDENA_POR'
    return t

def t_ES_NULO(t):
    r'IS\s+NULL'
    t.type = 'ES_NULO'
    return t

def t_CAMBIA_LA_TABLA(t):
    r'ALTER\s+TABLE'
    t.type = 'CAMBIA_LA_TABLA'
    return t

def t_AGREGA_LA_COLUMNA(t):
    r'ADD\s+COLUMN'
    t.type = 'AGREGA_LA_COLUMNA'
    return t

def t_ELIMINA_LA_COLUMNA(t):
    r'DROP\s+COLUMN'
    t.type = 'ELIMINA_LA_COLUMNA'
    return t

def t_CREA_LA_TABLA(t):
    r'CREATE\s+TABLE'
    t.type = 'CREA_LA_TABLA'
    return t

def t_TIRA_LA_TABLA(t):
    r'DROP\s+TABLE'
    t.type = 'TIRA_LA_TABLA'
    return t

def t_CLAVE_PRIMA(t):
    r'PRIMARY\s+KEY'
    t.type = 'CLAVE_PRIMA'
    return t

def t_CLAVE_REFERENTE(t):
    r'FOREIGN\s+KEY'
    t.type = 'CLAVE_REFERENTE'
    return t

t_COMMA = r','
t_EQUALS = r'='
t_STRING = r"'[^']*'"
t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STAR = r'\*'

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
    data = input("Type query:\n")
    lexer.input(data)
    # SELECT nombre FROM empleados WHERE EXISTS (SELECT 1 FROM proyectos WHERE id = departamento_id)
    sql_query = ""
    for tok in lexer:
        sql_query += tok.value + " " if (tok.type in ['IDENTIFIER', 'COMMA', 'EQUALS', 'NUMBER', 'STRING', 'LPAREN', 'RPAREN', 'STAR']) else tok.type.replace('_', ' ') + " "
    
    print(sql_query.strip() + "\n")
    validator.validate_sql_syntax(sql_query)
