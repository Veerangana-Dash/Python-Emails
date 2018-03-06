import csv 
import datetime
import shutil

from tempfile import NamedTemporaryFile

def get_length(file_path):
	with open("data.csv","r") as csvfile:
		reader=csv.reader(csvfile)
		reader_list=list(reader)
		return len(reader_list)

def append_data(file_path,name,email):
	fieldnames=['id','name','email']
	#the number of rows
	next_id=get_length(file_path)
	with  open(file_path,"a") as csvfile:
		writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
		writer.writerow({
			"id":next_id,
			"name":name,
			"email":email,
			"sent":"",
			"amount":amount,
			"date":datetime.datetime.now(),
			})

#append_data("data.csv","Justin","bogusemail@gmail.com",123.45)

def edit_data(edit_id=None, email=None, amount=None,sent=None):
	filename="data.csv"
	temp_file=NamedTemporaryFile(delete=False)

	with open(filename,"r") as csvfile, temp_file:
		#read from original file
		reader= csv.DictReader(csvfile)
		fieldnames=['id','name','email','amount','sent','date']
		#write in temporary file
		writer=csv.DictWriter(temp_file,fieldnames=fieldnames)

		for row in reader:
			if edit_id is not None:
				if int(row['id'])==int(edit_id):
					row['amount']=amount
					row['sent']=sent
				elif email is not None and edit_id is None:
					if str(row['id'])==str(email):
						row['amount']=amount
						row['sent'] =sent
				else:
					pass
				writer.writerow(row)

		shutil.move(temp_file.name,filename)
		return True
	return False


edit_data(email='bogusemail.gmail.com',amount=99.99,sent='')
