#creating base excel sheet

file=open("ACMD.csv",'a+')
head=['Date', 'Locality', 'Ambulance Number', 'Driver Name']

writer=csv.writer()
writer.writerows([head])