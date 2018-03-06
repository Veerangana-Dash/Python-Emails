import csv

#Write
with open("data.csv","w+") as csvfile:
	writer=csv.writer(csvfile)
	writer.writerow(["Col 1","Col 2"])
	writer.writerow(["Data 1","Data 2"])

#Read
with open("data.csv","r") as csvfile:
	reader=csv.reader(csvfile)
	for row in reader:
		print(row)

#Append
with open("data.csv","a") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Data 3","Data 4"])

#Read as Dictionary
with open("data.csv","r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)

#Write as Dictionary
with open("data.csv","w") as csvfile:
	fieldnames=["id","title"]
	writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
	writer.writerow({"id":123,"title":"New title"})
