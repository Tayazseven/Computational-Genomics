import csv
import MySQLdb

db = MySQLdb.connect('localhost',user='tug51373')
cursor =  db.cursor()

drop_datbase = "DROP DATABASE tug51373_LungCancerGenes" # first delete the database for the testing trials

cursor.execute(drop_datbase)

datbase = "CREATE DATABASE tug51373_LungCancerGenes" #Create the database
cursor.execute(datbase)

choose_datbase = "USE tug51373_LungCancerGenes" #Create the table

cursor.execute(choose_datbase)


sql_table = """CREATE TABLE LUNG_CANCER_GENE_TABLE (
	integer_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY UNIQUE,
	sequence_id TEXT NOT NULL,
	gene_name TEXT NOT NULL,
	sequence TEXT NOT NULL,
	cds TEXT NOT NULL);"""

cursor.execute(sql_table)

data_file = open("seqout.tsv", "r") #reading the tsv file
data_reader =csv.reader(data_file, delimiter = '\t')

for row in data_reader: #reading the data
    integer_id = int(row[0])
    sequence_id = str(row[1])
    gene_name = str(row[2])
    sequence = str(row[3])
    cds = str(row[4])
    #print integer_id
    ##print sequence_id
    ##print sequence
    #print cds
    data = (integer_id,sequence_id,gene_name,sequence,cds)
    insert_data = """INSERT INTO LUNG_CANCER_GENE_TABLE VALUES (%d,"%s","%s","%s","%s");"""
    print data
    cursor.execute(insert_data % data) #inserting the data in to the tablse

db.commit()
db.close()
data_file.close()