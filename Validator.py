import sqlparse

class validator:

    @staticmethod
    def validate_sql_syntax(query):
        try:
            # Analiza y verifica si la query está bien formada
            parsed = sqlparse.parse(query)
            if not parsed:
                raise ValueError("La query no contiene ninguna sentencia válida.")
            print("La sintaxis SQL es válida.")
            return True
        except Exception as e:
            print(f"Error en la sintaxis SQL: {e}")
            return False