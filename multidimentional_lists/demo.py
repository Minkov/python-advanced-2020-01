class Matrix_Row:
    def __init__(self):
        self.cells = []

    def add_cell(self, value):
        self.cells.append(value)

    def find_position(self, symbol):
        if symbol in self.cells:
            return self.cells.index(symbol)
        return None

class Matrix:
    def __init__(self):
        self.rows  = []

    def add_row(self, row):
        self.rows.append(row)

    def find_position(self, symbol):
        for row in self.rows:
            position = row.find_position(symbol)
            if position:
                return position
        return None

m = Matrix()
m.add_row(....)

m.find_position('x')