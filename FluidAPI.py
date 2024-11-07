class SQLQueryBuilder:
    def __init__(self):
        self.query_parts = {
            "select": [],
            "from": None,
            "where": [],
            "group_by": [],
            "order_by": [],
            "join": [],
            "limit": None
        }

    def select(self, *columns):
        self.query_parts["select"].extend(columns)
        return self

    def from_table(self, table):
        self.query_parts["from"] = table
        return self

    def where(self, condition):
        self.query_parts["where"].append(condition)
        return self

    def group_by(self, *columns):
        self.query_parts["group_by"].extend(columns)
        return self

    def order_by(self, column, ascending=True):
        direction = "ASC" if ascending else "DESC"
        self.query_parts["order_by"].append(f"{column} {direction}")
        return self

    def join(self, table, on_condition):
        self.query_parts["join"].append(f"JOIN {table} ON {on_condition}")
        return self

    def limit(self, n):
        self.query_parts["limit"] = n
        return self

    def build(self):
        query = []

        # SELECT
        select_clause = ", ".join(self.query_parts["select"]) or "*"
        query.append(f"SELECT {select_clause}")

        # FROM
        if self.query_parts["from"]:
            query.append(f"FROM {self.query_parts['from']}")

        # JOIN
        if self.query_parts["join"]:
            query.extend(self.query_parts["join"])

        # WHERE
        if self.query_parts["where"]:
            where_clause = " AND ".join(self.query_parts["where"])
            query.append(f"WHERE {where_clause}")

        # GROUP BY
        if self.query_parts["group_by"]:
            group_by_clause = ", ".join(self.query_parts["group_by"])
            query.append(f"GROUP BY {group_by_clause}")

        # ORDER BY
        if self.query_parts["order_by"]:
            order_by_clause = ", ".join(self.query_parts["order_by"])
            query.append(f"ORDER BY {order_by_clause}")

        # LIMIT
        if self.query_parts["limit"] is not None:
            query.append(f"LIMIT {self.query_parts['limit']}")

        return " ".join(query) + ";"
    
if __name__ == '__main__':
    query = (
    SQLQueryBuilder()
    .select("nombre", "edad")
    .from_table("usuarios")
    .where("edad > 30")
    .order_by("nombre", ascending=True)
    .limit(10)
    .build()
    )

    print(query)