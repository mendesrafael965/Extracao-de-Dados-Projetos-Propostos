"""_summary_
"""
import xlsxwriter


class Excel():
    """_summary_
    """

    def __init__(self, data, save_path=''):
        self.__columns = list(data[0].keys())
        self.__rows = [list(result.values()) for result in data]
        self.__save_path = save_path

    def __max_size_columns_data_frame(self):
        """_summary_
        """
        sizes = []
        for i in range(len(self.__columns)):
            col_i = []
            col_i.append(len(self.__columns[i]))
            for j in range(len(self.__rows)):
                col_i.append(len(str(self.__rows[j][i])))
            sizes.append(max(col_i))
        return sizes

    def make_table(self, table_name, sheet_name,  title_table='', logo=''):
        """_summary_
        """ 
        if self.__save_path!='':
            table_name = self.__save_path+'\\'+table_name

        workbook = xlsxwriter.Workbook(table_name)
        worksheet = workbook.add_worksheet(sheet_name)

        fmt_title = workbook.add_format({
            'bold': True,
            'font_size': 24,
            'valign': 'top',
            'font_color': '#76933C',
            'border': 0})
        
        fmt_header = workbook.add_format({
            'bold': True,
            'font_name': 'Cambria',
            'font_size': '11',
            'valign': 'top',
            'border': 1})
        
        fmt_grids = workbook.add_format({
            'font_name': 'Calibri',
            'font_size': '11',
            'valign': 'top',
            'border': 1,
            'text_wrap': True
        })

        if title_table != '':
            worksheet.write(3, 2, title_table, fmt_title)
            worksheet.hide_gridlines(2)

        if logo != '':
            worksheet.insert_image('A2', logo)
            worksheet.hide_gridlines(2)

        for i, width in enumerate(self.__max_size_columns_data_frame()):
            if width > 145:
                width = 145
            worksheet.set_column(i, i, width+5)

        for column in range(len(self.__columns)):
            worksheet.write(0, column, self.__columns[column], fmt_header)

        for row in range(len(self.__rows)):
            for column in range(len(self.__columns)):
                worksheet.write(
                    row+1, column, self.__rows[row][column], fmt_grids)
        workbook.close()
