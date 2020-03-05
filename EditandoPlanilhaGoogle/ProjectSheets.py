import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://docs.google.com/spreadsheets/d/1RxpzYZuKvvAbUnMIYKl3jwDXgGp8MGx80CzpKZ2ElmU/edit#gid=0']
cred = ServiceAccountCredentials.from_json_keyfile_name('CredencialSheetsProject01.json', scope)
gc = gspread.authorize(cred) #Esta linha esta com erro.
wks = gc.open_by_key('1RxpzYZuKvvAbUnMIYKl3jwDXgGp8MGx80CzpKZ2ElmU')
worksheet = wks.get_worksheet(0)

#worksheet.update_acell('A1', 'Funfa')