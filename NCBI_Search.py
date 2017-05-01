import random
import time
from Bio import SeqIO   ## frmo BioPython import the SeqIO module. Used to import sequence data into a BioPython class called a SeqRecord
from Bio.Seq import Seq
from Bio import Entrez
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

cdsout = open("cds_out.txt", "w")


class Myclass:
    """ a class to hold a SeqRecord and its CDS
        sr is an instance of SeqRecord
        CDS is a string
    """

    def __init__(self, seqrecords):
        self.seqrecords = seqrecords

    def extrctCDS(self):
        for sequ in self.seqrecords:
            for f in sequ.features:
                if f.type == "CDS":
                    print sequ.seq, sequ.name
                    cdsout.write( str(sequ.name) + str(sequ.seq) + '\n')

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
        #for f in gbrecord.features:
        #    if f.type == 'CDS':
        #       print (gbrecord.seq)
        #        srlist.append(gbrecord.seq)
        srlist.append(gbrecord)
        fetchhandle.close()
        testclass = Myclass(srlist)
        testclass.extrctCDS()
        #print gbrecord.extrctCDS()
    except:
        print "not found"

