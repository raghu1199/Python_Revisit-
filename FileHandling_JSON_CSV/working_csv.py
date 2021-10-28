import csv

# Read Csv File
# with open("File_handling/names.csv",'r') as csvFile:
#     csvReader=csv.reader(csvFile,delimiter=",")
#     print(csvReader) # prints object of type iterator 
#     for line in csvReader:
#         print(line)

#read only Email
# with open("File_handling/names.csv","r") as csvFile:
#     csvReader=csv.reader(csvFile,delimiter=",")
#     next(csvReader) # to skip first line header
#     for line in csvReader:
#         print(line[2])

# Write Into Csv file
# Read from 1st csv file and Write Into 2nd Csv File
# with open("File_handling/names.csv","r") as rf:
#     csvReader=csv.reader(rf)
#     with open("File_handling/new_names.csv","w") as wf:
#         csvWriter=csv.writer(wf,delimiter="\t")

#         for line in csvReader:
#             csvWriter.writerow(line)

# Read with DictReader

# with open("File_handling/names.csv","r") as f:
#     csvReader=csv.DictReader(f)
#     for line in csvReader:
#         print(line)

# Write with DictWriter need 1) fieldnames and 2)writeheader()
with open("File_handling/names.csv","r") as rf:
    csvReader=csv.DictReader(rf)
    with open("File_handling/new_dict.csv","w") as wf:
        fieldnames=['first','last'] # fieldnames same as old file filednames must
        
        csvWriter=csv.DictWriter(wf,fieldnames=fieldnames,delimiter="\t")
        csvWriter.writeheader()
        for line in csvReader:
            del line['email']
            csvWriter.writerow(line)

