class DB:
    def __init__(self, meta_db, list_tables):
        self.meta_db = meta_db
    
    def insert(self, data):
        pass

    def update(self, data_update):
        pass

    def delete(self, data_delete):
        pass

    def select(self, query):
        pass


class Table:
    def __init__(self, meta_data_table, list_columns):
        pass

    def insert(self, data):
        pass

    def update(self, data_update):
        pass

    def delete(self, data_delete):
        pass

    def select(self, query):
        pass

#commentary
class Columen:
    def __init__(self, meta_columen_table):
        self.meta_columen_table=meta_columen_table

    def set_data(self, value):
        pass

    def check_type(self, value):
        pass