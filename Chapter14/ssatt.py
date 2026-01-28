import ezsheets

ss =  ezsheets.Spreadsheet("1ttfn5ow9LBWOZieTKk_5wanXYCQBHP4z15nASlA_M4s")
print(ss.title)

ss.title = "Class Data"

print(ss.spreadsheetId)
print(ss.url)
print(ss.sheetTitles)
print(ss.sheets)

print(ss[0])
print(ss["Students"])

ss.refresh()