
from Bio import SeqIO   ## frmo BioPython import the SeqIO module. Used to import sequence data into a BioPython class called a SeqRecord
from Bio import Entrez
import csv
import itertools
n_id = []
seq_id = []
seq_=[]
cds_=[]
class Myclass:
    """ a class to hold a SeqRecord and extracts the Coding sequence if the gene has it. Open the file and writes the Gene id,
    location of cds, coding sequence
    """

    def __init__(self, seqrecords):
        self.seqrecords = seqrecords

    def extrctCDS(self):
        for sequ in self.seqrecords:
            n_id.append(str(sequ.name)) #appending sequence id
            seq_id.append(str(sequ.description)) #description
            seq_.append(str(sequ.seq)) #sequence
            for f in sequ.features:
                if f.type == "CDS": #checking the 'type' of SeqRecord results and extracting the CDS part
                    cds_.append(f.extract(sequ.seq)) #coding sequence

Entrez.email = "tug51373@temple.edu" ##online requrests using Entrez  should include a valid email address

resulthandle = Entrez.esearch(db="gene", retmax=10, term="(lung cancer[Disease/Phenotype]) AND 9606[Taxonomy ID]")
ereaddic = Entrez.read(resulthandle)  ## make a dictionary from the results.
resulthandle.close()

## get accession numbers for the Gene ID numbers in ereaddic["IdList"]
fetchhandle = Entrez.efetch(db="nucleotide", id=ereaddic["IdList"], rettype="acc")
accnums = fetchhandle.read().splitlines()
fetchhandle.close()

srlist=[] #list of Seqrecords
for accnum in accnums:
    print accnum,
    try:
        print "found"
        fetchhandle = Entrez.efetch(db="nucleotide", id=accnum, rettype="gb", retmode="text")
        gbrecord = (SeqIO.read(fetchhandle, "genbank"))

        srlist.append(gbrecord)
        fetchhandle.close()

    except:
        print "not found"
testclass = Myclass(srlist)
testclass.extrctCDS()

query_id = [] #integer id
for i in range(0,len(cds_)):
    query_id.append(i+1)
#print query_id
#with open('seqout.tsv', 'wb') as f: #writing to tsv file
#    a = csv.writer(f, delimiter='\t')
#    a.writerows(zip(query_id,n_id,seq_id,seq_, cds_))

