import pandas as pd

class Excel_Reader:
    def __init__(self, file_name):
        self.sheetDataFrame = pd.read_excel(f'working_files/{file_name}.xlsx')

    def getColumnWithSep(self, col_name):
        self.column = self.sheetDataFrame[f'{col_name}']
        self.column_list = self.column.tolist()
        print()
        print(', '.join(map(str, self.column_list)))
        print()
        return

    def getRowWithSep(self, row_name):
        self.row = self.sheetDataFrame[f'{row_name}']
        self.row_list = self.row.tolist()
        print()
        print(', '.join(map(str, self.row_list)))
        print()
        return

    def getXSection(self, row, column):
        self.value = self.sheetDataFrame.at[row, column]
        print()
        print(self.value)
        print()
        return