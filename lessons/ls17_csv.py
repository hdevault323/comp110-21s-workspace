"""Example reading csv files."""

#first, import capabilities

from csv import DictReader 

#let python implicitly decide what file type this is
#we want to open weather.csv
#trust that when we open a file that it will be in a type 
file_handle = open("data/weather.csv", "r", encoding="utf8") #specify that yuo are working in utf8
csv_reader = DictReader(file_handle)
#opening file, telling operstinf system we are tryig to open a file, that file is a csv file and 
#fetting more soecific, saying ik this is a csv file and i want to read each row


#a table can be modeled as a list of rows where a row 
# is a dictionary with the column title as the key
table: list[dict[str, str]] = []


#Add each row of data to our table 
for row in csv_reader: 
    table.append(row)
    # print(row)# when you use csv reader in a for in it moves through each line, uses each line as a header
    #then each row returns a dictionary and then the value is that particular column value


#when were done reading/working with a file, we should close it!
file_handle.close()

print(table)


#calculate average high temp
#process the table by a specific column
high_temps: list[float] = []
for row in table:
        high_temps.append(float(row["high"]))
print(high_temps)


print("The average high temp was: ")
avg_high: float = sum(high_temps) / len(high_temps)
print(avg_high)