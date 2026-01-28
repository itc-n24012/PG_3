import ezsheets

ss = ezsheets.createSpreadsheet("My Spreadsheet")
sheet = ss[0]
print(sheet.title)

sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["C1"] = "Favorite Movie"

print(sheet["A1"])
print(sheet["A2"]) #まだ何も入ってない
print(sheet[2,1]) #いわば"B1"

#2行目のセルに値をセット
sheet["A2"] = "tanitan"
sheet["B2"] = "5"
sheet["C2"] = "korea movies"
