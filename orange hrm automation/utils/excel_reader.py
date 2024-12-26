import openpyxl


def get_credentials(file_path):
    workbook = openpyxl.load_workbook("C:\Arun\code\orange hrm automation\data\cerdentials.xlsx")
    sheet = workbook.active
    credentials = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        credentials.append((row[4], row[5]))
    return credentials
